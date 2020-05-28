from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import CriacaoUsusarioForm, PerfilForm, ContaUsuarioForm
from .models import Perfil
from .tokens import contas_token_ativacao

#view para tratamento do formulário de registro de novo usuário
def paginaRegistro(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CriacaoUsusarioForm()
        if request.method == 'POST':
            form = CriacaoUsusarioForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.is_active = False
                user.save()
                
                # Definição do envio de email quando o formulário de registro é enviado e é válido
                current_site = get_current_site(request)
                assunto = 'Ativação da conta WPlus'
                menssagem = render_to_string('emails/ativacao_conta.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': contas_token_ativacao.make_token(user),
                })
                email_para = form.cleaned_data.get('email')
                email = EmailMessage
                user.email_user(assunto, menssagem) 

                messages.success(request, 'Conta criada para o usuario ' + user.username + ' Porfavor clique no link de confirmação enviado para seu email para completar o registro.')        
                return redirect('obrigado')   

        context = {'form': form}
        return render(request, 'contas/registrar.html', context)


def paginaLogin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            senha = request.POST.get('senha')

            user = authenticate(request, username=username, password=senha)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Nome do usuário ou senha incorretos!')

        context = {}
        return render(request, 'contas/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def paginaObrigado(request):
    context = {}
    return render(request, 'contas/pagina_obrigado.html', context)


#Decorator para acessar a pagina de dashboard, apenas se o usuário estiver logado, cao não, direciona para pagina de login
@login_required(login_url='login')
def userDashboardPerfil(request):
    perfil = request.user.perfil

    form_conta = ContaUsuarioForm(instance=request.user)
    form = PerfilForm(instance=perfil)
       

    if request.method == 'POST':
        form_conta = ContaUsuarioForm(request.POST, instance=request.user)
        if form_conta.is_valid():
            form_conta.save()

    context = {'form': form}
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()


    context = {
        'form': form,
        'form_conta': form_conta,        
    }

    return render(request, 'contas/user_dashboard_perfil.html', context)


#Decorator para acessar a pagina de dashboard, apenas se o usuário estiver logado, cao não, direciona para pagina de login
@login_required(login_url='login')
def userDashboardConta(request):


    context = {}
    return render(request, 'contas/user_dashboard_conta.html', context)


# função para validação da conta e ativação do usuário
def ativacaoConta(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and contas_token_ativacao.check_token(user, token):
        user.is_active = True
        user.perfil.email_confirmado = True
        user.save()
        login(request, user)

        messages.success(request, ('Sua conta foi confirmada.'))
        return redirect('dashboard')
    else:
        messages.warning(request, ('O link de confirmação é inválido, possivelmente ele já foi utilizado.'))
        return redirect('')

def paginaCheckout(request):
    context = {}
    return render(request, 'contas/checkout.html', context)
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CriacaoUsusarioForm, ClienteForm
from .models import Cliente

def paginaRegistro(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CriacaoUsusarioForm()
        if request.method == 'POST':
            form = CriacaoUsusarioForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Conta criada para o usuario ' + user)        
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


@login_required(login_url='login')
def userDashboard(request):
    cliente = request.user.cliente
    form = ClienteForm(instance=cliente)

    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'contas/user_dashboard.html', context)


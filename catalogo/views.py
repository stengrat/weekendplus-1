from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse

from .models import Filmes, Series, FavoritosFilmes
from .forms import FilmeForm

# Create your views here.

def paginaFilmesSeries(request):
    filmes = Filmes.objects.order_by('-id')[:6]
    series = Series.objects.order_by('-id')[:6]
    ultimos = Filmes.objects.all().order_by('-id')[:6]
    last_upload = Filmes.objects.all().order_by('-id')[:1]

    form = FilmeForm()
    if(request.method == 'POST'):
        form = FilmeForm(request.POST)
        if form.is_valid():
            filme = form.save()
            filme.user_id = request.user
            filme.save()
            print('boa')
   
    context = {
        'filmes': filmes, 
        'series': series, 
        'ultimos': ultimos,
        'last_upload': last_upload,
        'form': form
    }
    return render(request, 'catalogo/pagina_filmes_series.html', context)

def paginaFilmes(request):
    filmes = Filmes.objects.order_by('-id')[:6]
    last_upload = Filmes.objects.all().order_by('-id')[:1]

    context = {
        'filmes': filmes,
        'last_upload': last_upload
    }
    return render(request, 'catologo/pagina_filmes.html', context)

def paginaMidiaDescricao(request):
    data = {'success': False}
    if(request.method == 'POST'):
        filme = request.POST.get('userfilme')
        fav = FavoritosFilmes()
        fav.user_id = request.user
        fav.filme_id = filme
        fav.save()
        data['success'] = True
        print('Boa')
    context = {}
    return render(request, 'catalogo/midia_descricao.html', context)


def paginaFavoritos(request):
    user = request.user
    filmes = FavoritosFilmes.objects.all().filter(user_id=user).order_by('-id')

    context = {
        'filmes': filmes,
    }

    return render(request, 'catalogo/favoritos.html', context)

def favoritosDelete(request, id):
    favorito = FavoritosFilmes.objects.get(id=id)
    favorito.delete()
    return redirect('favoritos')
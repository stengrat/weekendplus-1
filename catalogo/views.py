from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Filmes, Series

# Create your views here.

def paginaFilmesSeries(request):
    filmes = Filmes.objects.order_by('-id')[:6]
    series = Series.objects.order_by('-id')[:6]
    ultimos = Filmes.objects.all().order_by('-id')[:6]
    last_upload = Filmes.objects.all().order_by('-id')[:1]
   
    context = {
        'filmes': filmes, 
        'series': series, 
        'ultimos': ultimos,
        'last_upload': last_upload
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
    context = {}
    return render(request, 'catalogo/midia_descricao.html', context)
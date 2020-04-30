from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import Midia

# Create your views here.

def paginaFilmesSeries(request):
    filmes = Midia.objects.filter(categoria = "Filme").order_by('-id')[:6]
    series = Midia.objects.filter(categoria = "Serie").order_by('-id')[:6]
    ultimos = Midia.objects.all().order_by('-id')[:6]
    last_upload = Midia.objects.all().order_by('-id')[:1]
   
    context = {
        'filmes': filmes, 
        'series': series, 
        'ultimos': ultimos,
        'last_upload': last_upload
    }
    return render(request, 'midia/pagina_filmes_series.html', context)

def paginaFilmes(request):
    filmes = Midia.objects.filter(categoria = "Filme").order_by('-id')[:6]
    last_upload = Midia.objects.all().order_by('-id')[:1]

    context = {
        'filmes': filmes,
        'last_upload': last_upload
    }
    return render(request, 'midia/pagina_filmes.html', context)

def paginaMidiaDescricao(request):
    context = {}
    return render(request, 'midia/midia_descricao.html', context)
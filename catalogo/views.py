from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse

from .models import Filmes, Series, FavoritosFilmes, FavoritosSeries
from .forms import FilmeForm, SerieForm

# Create your views here.

def paginaSeries(request):
    series = Series.objects.order_by('id')[:6]
    ultimos_series = Series.objects.all().order_by('-id')[:6]
    last_upload = Series.objects.all().order_by('-id')[:1]   
                 
    form_serie = SerieForm()
    if request.method == 'POST' and 'btn-serie' in request.POST:
        form_serie = SerieForm(request.POST)
        if form_serie.is_valid():
            serie = form_serie.save()
            serie.user_id = request.user
            serie.save()
    
    context = {
        'series': series, 
        'ultimos_series': ultimos_series,
        'last_upload': last_upload,
        'form_serie': form_serie
    }
    return render(request, 'catalogo/pagina_series.html', context)

def paginaFilmes(request):
    filmes = Filmes.objects.order_by('id')
    ultimos_filmes = Filmes.objects.all().order_by('-id')[:6]
    last_upload = Filmes.objects.all().order_by('-id')[:1]
    diretores = Filmes.objects.values_list("diretor", flat=True).order_by("diretor").distinct()
    anos = Filmes.objects.values_list("ano", flat=True).order_by("ano").distinct()
    generos = Filmes.objects.values_list("genero", flat=True).order_by("genero").distinct()

    form = FilmeForm()
    if request.method == 'POST' and 'btn-filme' in request.POST:
        form = FilmeForm(request.POST)
        if form.is_valid():
            filme = form.save()
            filme.user_id = request.user
            filme.save()

    context = {
        'filmes': filmes,
        'ultimos_filmes': ultimos_filmes,
        'form': form,
        'last_upload': last_upload,
        'diretores': diretores,
        'anos': anos,
        'generos': generos,
    }
    return render(request, 'catalogo/pagina_filmes.html', context)

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

def paginaSeriesDescricao(request):
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
    return render(request, 'catalogo/series_descricao.html', context)


def paginaFavoritos(request):
    user = request.user
    filmes = FavoritosFilmes.objects.all().filter(user_id=user).order_by('-id')
    series = FavoritosSeries.objects.all().filter(user_id=user).order_by('-id')

    context = {
        'filmes': filmes,
        'series': series,
    }

    return render(request, 'catalogo/favoritos.html', context)

def favoritosDeleteFilme(request, id):
    favorito = FavoritosFilmes.objects.get(id=id)
    favorito.delete()
    return redirect('favoritos')

def favoritosDeleteSerie(request, id):
    favorito = FavoritosSeries.objects.get(id=id)
    favorito.delete()
    return redirect('favoritos')


def paginaDescricaoFilme(request, id):
    filme = get_object_or_404(Filmes, id=id)
    context = {'filme': filme}
    return render(request, 'catalogo/filme_descricao.html', context)

def paginaDescricaoSerie(request, id):
    serie = get_object_or_404(Series, id=id)
    context = {'serie':serie}
    return render(request, 'catalogo/pagina_detalhe_serie', context)

def paginaFilmeGenero(request):
    diretores = Filmes.objects.values_list("diretor", flat=True).order_by("diretor").distinct()
    anos = Filmes.objects.values_list("ano", flat=True).order_by("ano").distinct()
    generos = Filmes.objects.values_list("genero", flat=True).order_by("genero").distinct()
    if request.method == "POST":
        filtro = request.POST['genero']
        filmes = Filmes.objects.filter(genero=filtro).all()
    
    context = {
        'filmes':filmes,
        'diretores': diretores,
        'anos': anos,
        'generos': generos,
    }

    return render(request, 'catalogo/filme-filtrado.html', context)

def paginaFilmeDiretor(request):
    diretores = Filmes.objects.values_list("diretor", flat=True).order_by("diretor").distinct()
    anos = Filmes.objects.values_list("ano", flat=True).order_by("ano").distinct()
    generos = Filmes.objects.values_list("genero", flat=True).order_by("genero").distinct()
    if request.method == "POST":
        filtro = request.POST['diretor']
        filmes = Filmes.objects.filter(diretor=filtro).all()
    
    context = {
        'filmes':filmes,
        'diretores': diretores,
        'anos': anos,
        'generos': generos,
    }

    return render(request, 'catalogo/filme-filtrado.html', context)

def paginaFilmeAno(request):
    diretores = Filmes.objects.values_list("diretor", flat=True).order_by("diretor").distinct()
    anos = Filmes.objects.values_list("ano", flat=True).order_by("ano").distinct()
    generos = Filmes.objects.values_list("genero", flat=True).order_by("genero").distinct()
    if request.method == "POST":
        filtro = request.POST['ano']
        filmes = Filmes.objects.filter(ano=filtro).all()
    
    context = {
        'filmes':filmes,
        'diretores': diretores,
        'anos': anos,
        'generos': generos,
    }
    
    return render(request, 'catalogo/filme-filtrado.html', context)
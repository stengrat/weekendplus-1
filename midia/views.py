from django.shortcuts import render

from .models import Midia

# Create your views here.

def paginaFilmesSeries(request):
    filmes = Midia.objects.filter(categoria = "Filme")
    series = Midia.objects.filter(categoria = "Serie")
    ultimos = Midia.objects.all().order_by('-id')[:10]

    context = {'filmes': filmes, 'series': series, 'ultimos':ultimos}
    return render(request, 'midia/pagina_filmes_series.html', context)
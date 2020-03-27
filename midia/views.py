from django.shortcuts import render

from .models import Midia

# Create your views here.

def paginaFilmesSeries(request):
    filmes = Midia.objects.filter(categoria = "Filme")

    context = {'filmes': filmes}
    return render(request, 'midia/pagina_filmes_series.html', context)
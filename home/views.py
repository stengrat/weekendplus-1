from django.shortcuts import render

def paginaInicial(request):
    context = {}
    return render(request, 'home/home.html', context)



from django.shortcuts import render

def paginaInicial(request):
    context = {}
    return render(request, 'home/index.html', context)



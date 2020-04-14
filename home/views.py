from django.shortcuts import render

def paginaInicial(request):
    context = {}
    return render(request, 'home/home.html', context)


def error_404(request):
    context = {}
    return render(request, 'home/404.html', context)


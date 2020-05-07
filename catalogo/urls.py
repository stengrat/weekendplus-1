from django.urls import path
from . import views

urlpatterns = [
    path('filmes-series/', views.paginaFilmesSeries, name='filmes-series'),
    path('filmes/', views.paginaFilmes, name='filmes'),
    path('filme-descricao/', views.paginaMidiaDescricao, name='filme-descricao')

]
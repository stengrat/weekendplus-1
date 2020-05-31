from django.urls import path
from . import views

urlpatterns = [
    path('series/', views.paginaSeries, name='series'),
    path('filmes/', views.paginaFilmes, name='filmes'),
    path('filme-descricao/', views.paginaMidiaDescricao, name='filme-descricao'),
    path('series-descricao/', views.paginaSeriesDescricao, name='series-descricao'),
    path('favoritos/', views.paginaFavoritos, name='favoritos'),
    path('delete_filme/<int:id>', views.favoritosDeleteFilme, name='delete_filme'),
    path('delete_serie/<int:id>', views.favoritosDeleteSerie, name='delete_serie'),
]
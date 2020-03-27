from django.urls import path
from . import views

urlpatterns = [
    path('filmes-series/', views.paginaFilmesSeries, name='filmes-series')

]
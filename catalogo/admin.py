from django.contrib import admin
from .models import Filmes, Series, FavoritosFilmes, SerieEpisodio

admin.site.register(Filmes)
admin.site.register(Series)
admin.site.register(FavoritosFilmes)
admin.site.register(SerieEpisodio)
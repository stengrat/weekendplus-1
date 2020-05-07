from django.contrib import admin
from .models import Filmes, Series, FavoritosFilmes

admin.site.register(Filmes)
admin.site.register(Series)
admin.site.register(FavoritosFilmes)
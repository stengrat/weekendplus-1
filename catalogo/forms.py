from django import forms
from django.forms import ModelForm

from .models import *

class FilmeForm(ModelForm):
    class Meta:
        model = FavoritosFilmes
        fields = ('filme_id',)

class SerieForm(ModelForm):
    class Meta:
        model = FavoritosSeries
        fields = ('serie_id',)
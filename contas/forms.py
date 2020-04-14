from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


#  classe para criar o formulário de atualização dos dados na página de dashboard do usuário
class ContaUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


# formulário de cadastro do usuário
class CriacaoUsusarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

# Formulário de atualização do perfil para dashboard do usuário
class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        exclude = ['user', 'email_confirmado', 'imagem_perfil']

# Formulário de atualização da imagem do perfil para dashboard do usuário
#class ImagemPerfilForm(ModelForm):
#    class Meta:
#        model = Perfil
#        fields = 'imagem_perfil'
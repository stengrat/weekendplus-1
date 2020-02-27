from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


class CriacaoUsusarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = ['user']
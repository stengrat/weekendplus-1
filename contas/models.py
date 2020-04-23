from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Teste(models.Model):
    teste1 = models.CharField(max_length=100, null=True)

class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email_confirmado = models.BooleanField(default=False)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    pais = models.CharField(max_length=20, null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=20, null=True, blank=True)
    logradouro = models.CharField(max_length=200, null=True, blank=True)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    imagem_perfil = models.ImageField(default='user_image.png', null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()

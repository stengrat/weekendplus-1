from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email_confirmado = models.BooleanField(default=False)
    telefone = models.CharField(max_length=20, null=True)
    cep = models.CharField(max_length=10, null=True)
    pais = models.CharField(max_length=20, null=True)
    estado = models.CharField(max_length=20, null=True)
    cidade = models.CharField(max_length=20, null=True)
    logradouro = models.CharField(max_length=200, null=True)
    complemento = models.CharField(max_length=200, null=True)
    numero = models.IntegerField(null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    imagem_perfil = models.ImageField(default='user_image.png', null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def update_user_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
        instance.profile.save()

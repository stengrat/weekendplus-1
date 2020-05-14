from django.db import models
from django.contrib.auth.models import User

class Filmes(models.Model):

    GENERO_LIST = (
        ('Ação','Ação'),
        ('Anime','Anime'),
        ('Aventura','Aventura'),
        ('Clássicos','Clássicos'),
        ('Comédia','Comédia'),
        ('Documentário','Documentário'),
        ('Drama','Drama'),
        ('Fantasia','Fantasia'),
        ('Ficção Científica','Ficção Científica'),
        ('Musicais','Musicais'),
        ('Policiais','Policiais'),
        ('Romance','Romance'),
        ('Suspense','Suspense'),
        ('Terror','Terror'),
    )

    CLASSIFICACAO_LIST = (
        ('L','Livre'),
        ('10','10'),
        ('12','12'),
        ('14','14'),
        ('16','16'),
        ('18','18'),
    )

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    ano = models.IntegerField()
    duracao = models.CharField(max_length=20)
    diretor = models.CharField(max_length=100)
    genero = models.CharField(max_length=20, choices=GENERO_LIST)
    classificacao = models.CharField(max_length=20, choices=CLASSIFICACAO_LIST)
    link = models.URLField(max_length=500, null=True)
    thumbnail = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.titulo


class Series(models.Model):

    GENERO_LIST = (
        ('Ação','Ação'),
        ('Anime','Anime'),
        ('Aventura','Aventura'),
        ('Clássicos','Clássicos'),
        ('Comédia','Comédia'),
        ('Documentário','Documentário'),
        ('Drama','Drama'),
        ('Fantasia','Fantasia'),
        ('Ficção Científica','Ficção Científica'),
        ('Musicais','Musicais'),
        ('Policiais','Policiais'),
        ('Romance','Romance'),
        ('Suspense','Suspense'),
        ('Terror','Terror'),
    )

    CLASSIFICACAO_LIST = (
        ('L','Livre'),
        ('10','10'),
        ('12','12'),
        ('14','14'),
        ('16','16'),
        ('18','18'),
    )

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    ano = models.IntegerField()
    duracao = models.CharField(max_length=20)
    diretor = models.CharField(max_length=100)
    genero = models.CharField(max_length=20, choices=GENERO_LIST)
    classificacao = models.CharField(max_length=20, choices=CLASSIFICACAO_LIST)
    temporadas = models.IntegerField()
    link = models.URLField(max_length=500, null=True)
    thumbnail = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.titulo

class FavoritosFilmes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    filme_id = models.ForeignKey(Filmes, on_delete=models.CASCADE, null=True)
    horario = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = (("user_id", "filme_id"),)

class FavoritosSeries(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    serie_id = models.ForeignKey(Series, on_delete=models.CASCADE, null=True)
    horario = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = (("user_id", "serie_id"),)
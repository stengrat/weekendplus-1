from django.db import models

class Midia(models.Model):

    CATEGORIA_LIST = (
        ('Filme','Filme'),
        ('Serie','Serie'),
    )

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
    categoria = models.CharField(max_length=20, choices=CATEGORIA_LIST)
    genero = models.CharField(max_length=20, choices=GENERO_LIST)
    classificacao = models.CharField(max_length=20, choices=CLASSIFICACAO_LIST)
    link = models.URLField(max_length=500, null=True)
    thumbnail = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.titulo



from django.db import models

# Create your models here.
class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)
    ano = models.IntegerField()

    def __str__(self):
        return self.titulo
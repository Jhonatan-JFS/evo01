from django.db import models

# Create your models here.
class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)
    ano = models.IntegerField()

    def __str__(self):
        return self.titulo

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=150)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.assunto}"
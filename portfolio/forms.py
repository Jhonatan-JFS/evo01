from django import forms;
from .models import Projeto, Contato;

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'categoria', 'ano']

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']

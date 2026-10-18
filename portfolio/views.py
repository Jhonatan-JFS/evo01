from django.shortcuts import render, redirect;
from django.contrib.auth.decorators import login_required;
from django.core.exceptions import PermissionDenied;

from .models import Projeto;
from .forms import ProjetoForm;

def index(request):
    projetos = Projeto.objects.order_by('-ano', 'titulo')
    
    contexto ={
        'nome': 'John_JFS',
        'area': 'Tecnologia',
        'especialidade': 'Desenvolvimento e Suporte de TI',
        'tecnologias': [
            'Python',
            'Django',
            'HTML',
            'CSS',
            'JavaScript',
            'Redes de Computadores',
            'Suporte Técnico',
        ],
        'projetos': projetos,
    }
    return render(request, 'portfolio/index.html', contexto)

def contato(request):
    return render(request, 'portfolio/contato.html')

@login_required(login_url='admin:login')
def adicionar(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProjetoForm()

    return render(
        request,
        'portfolio/adicionar.html',
        {'form': form}
    )
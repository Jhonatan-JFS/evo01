from django.shortcuts import render, redirect, get_object_or_404;
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

def detalhe(request, id):
    projeto = get_object_or_404(Projeto, id=id)

    contexto = {
        'projeto': projeto,
    }

    return render(
        request,
        'portfolio/detalhe.html',
        contexto
    )

@login_required(login_url='admin:login')
def editar(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    projeto = get_object_or_404(Projeto, id=id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        
        if form.is_valid():
            form.save()
            return redirect('detalhe', id=projeto.id)
    else:
        form = ProjetoForm(instance=projeto)

    contexto = {
        'form': form,
        'projeto': projeto,
    }

    return render(
        request,
        'portfolio/editar.html',
        contexto
    )
@login_required(login_url='admin:login')
def excluir(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    projeto = get_object_or_404(Projeto, id=id)

    if request.method == 'POST':
        projeto.delete()
        return redirect('index')

    return render(
        request,
        'portfolio/excluir.html',
        {'projeto': projeto}
    )
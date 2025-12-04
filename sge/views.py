
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .forms import PessoaForm

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/lista.html', {'pessoas': pessoas})

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm()
    
    return render(request, 'pessoas/criar.html', {'form': form})

def alterar_pessoa(request, id_pessoa):
    pessoa = get_object_or_404(Pessoa, pk=id_pessoa)
    
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    
    return render(request, 'pessoas/criar.html', {'form': form})

def excluir_pessoa(request, id_pessoa):
    pessoa = get_object_or_404(Pessoa, pk=id_pessoa)
    pessoa.delete()
    return redirect('lista_pessoas')
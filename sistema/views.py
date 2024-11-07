from django.shortcuts import render, redirect
from .models import Empresa

def index(request):
    return render(request, 'index.html')

def empresas(request):
    empresas = Empresa.objects.all()
    context = {
        'emp': empresas
    }
    return render(request, 'empresas.html', context)

def adicionar_empresa(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        
        # Cria a nova empresa
        Empresa.objects.create(
            nome=nome,
            telefone=telefone,
            endereco=endereco
        )
        
        # Redireciona para a página de empresas
        return redirect('empresas')

def deletar_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    return redirect('empresas')

def editar(request, id):
    empresa = Empresa.objects.get(id=id)
    context = {
        'emp': empresa
    }
    return render(request, 'update_empresa.html', context)

def update(request, id):
    if request.method == "POST":
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        empresa = Empresa.objects.get(id=id)

        empresa.nome = nome
        empresa.telefone = telefone
        empresa.endereco = endereco

        empresa.save()
        # Redireciona para a página de empresas
        return redirect('empresas')

def pagina_adicionar_empresa(request):
    return render(request, 'add_empresa.html')

def funcionarios(request):
    return render(request, 'funcionarios.html')
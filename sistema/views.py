from django.shortcuts import render, redirect
from .models import Empresa, Funcionario, Ponto

def index(request):
    return render(request, 'index.html')

def empresas(request):
    empresas = Empresa.objects.all()
    context = {
        'emp': empresas
    }
    return render(request,'empresas.html' , context)

def adicionar_empresa(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        
        Empresa.objects.create(
            nome=nome,
            telefone=telefone,
            endereco=endereco
        )
        
        return redirect('empresas')

def deletar_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    return redirect('empresas')

def editar_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    context = {
        'emp': empresa
    }
    return render(request, 'update_empresa.html', context)

def update_empresa(request, id):
    if request.method == "POST":
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        empresa = Empresa.objects.get(id=id)

        empresa.nome = nome
        empresa.telefone = telefone
        empresa.endereco = endereco

        empresa.save()
        return redirect('empresas')

def pagina_adicionar_empresa(request):
    return render(request, 'add_empresa.html')

## ------------------------------------------------------------

def funcionarios(request):
    funcionarios = Funcionario.objects.all()
    context = {
        'func': funcionarios
    }
    return render(request, 'funcionarios.html', context)

def adicionar_funcionario(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        empresa_id = request.POST.get('empresa')
        empresa = Empresa.objects.get(id=empresa_id)

        Funcionario.objects.create(
            nome=nome,
            email=email,
            empresa=empresa
        )

        return redirect('funcionarios')

def deletar_funcionario(request, id):
    funcionario = Funcionario.objects.get(id=id)
    funcionario.delete()
    return redirect('funcionarios')

def editar_funcionario(request, id):
    funcionario = Funcionario.objects.get(id=id)
    empresa = Empresa.objects.all()
    context = {
        'func': funcionario,
        'emp': empresa
    }
    return render(request, 'update_funcionario.html', context)

def update_funcionario(request, id):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        empresa_id = request.POST.get('empresa')
        empresa = Empresa.objects.get(id=empresa_id)

        funcionario = Funcionario.objects.get(id=id)

        funcionario.nome = nome
        funcionario.email = email
        funcionario.empresa = empresa

        funcionario.save()
        return redirect('funcionarios')

def pagina_adicionar_funcionario(request):
    empresas = Empresa.objects.all()
    context = {
        'emp': empresas
    }
    return render(request, 'add_funcionario.html', context)

## -------------------------------------

def ponto(request):
    pontos = Ponto.objects.all()
    context = {
        'pt': pontos
    }
    return render(request,'ponto.html' , context)

def pagina_adicionar_ponto(request):
    return render(request, 'add_ponto.html')

def adicionar_ponto(request):
    if request.method == "POST":
        funcionario_email = request.POST.get('email')
        entrada = request.POST.get('entrada')
        saida = request.POST.get('saida')


        funcionario = Funcionario.objects.get(email=funcionario_email)

        Ponto.objects.create(
            funcionario=funcionario,
            entrada=entrada,
            saida=saida
        )

        return redirect('ponto')
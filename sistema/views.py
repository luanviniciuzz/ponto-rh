from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def funcionarios(request):
    return render(request, 'funcionarios.html')

def empresas(request):
    return render(request, 'empresas.html')
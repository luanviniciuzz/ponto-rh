from django.urls import path
from sistema.views import index , funcionarios, empresas

urlpatterns = [
  path('', index, name='mysite'),
  path('funcionarios/', funcionarios, name='funcionarios'),
  path('empresas/', empresas, name='empresas')
]
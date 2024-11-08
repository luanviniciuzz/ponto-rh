from django.urls import path
from sistema.views import index, adicionar_empresa, empresas, pagina_adicionar_empresa, deletar_empresa, editar_empresa, update_empresa
from sistema.views import funcionarios, pagina_adicionar_funcionario, adicionar_funcionario, deletar_funcionario, update_funcionario, editar_funcionario
from sistema.views import ponto, pagina_adicionar_ponto, adicionar_ponto

urlpatterns = [
    path('', index, name='mysite'),
    ## MODULO EMPRESAS
    path('empresas/', empresas, name='empresas'),
    path('empresas/adicionar/', pagina_adicionar_empresa, name='pagina_adicionar_empresa'),
    path('adicionar_empresa/', adicionar_empresa, name='adicionar_empresa'),
    path('deletar_empresa/<int:id>', deletar_empresa, name='deletar_empresa'),
    path('editar/empresa/<int:id>', editar_empresa, name='editar_empresa'),
    path('update/empresa/<int:id>', update_empresa, name='update_empresa'),
    ## MODULO FUNCIONARIOS
    path('funcionarios/', funcionarios, name='funcionarios'),
    path('funcionario/adicionar/', pagina_adicionar_funcionario, name='pagina_adicionar_funcionario'),
    path('adicionar_funcionario/', adicionar_funcionario, name='adicionar_funcionario'),
    path('deletar_funcionario/<int:id>', deletar_funcionario, name='deletar_funcionario'),
    path('editar/funcionario/<int:id>', editar_funcionario, name='editar_funcionario'),
    path('update/funcionario/<int:id>', update_funcionario, name='update_funcionario'),
    ## MODULO PONTO
    path('ponto/', ponto, name='ponto'),
    path('ponto/adicionar/', pagina_adicionar_ponto, name='pagina_adicionar_ponto'),
    path('adicionar_ponto/', adicionar_ponto, name='adicionar_ponto'),
]

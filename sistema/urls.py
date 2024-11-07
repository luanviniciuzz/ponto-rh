from django.urls import path
from sistema.views import index, funcionarios, adicionar_empresa, empresas, pagina_adicionar_empresa, deletar_empresa, editar, update

urlpatterns = [
    path('', index, name='mysite'),
    ## MODULO EMPRESAS
    path('empresas/', empresas, name='empresas'),
    path('empresas/adicionar/', pagina_adicionar_empresa, name='pagina_adicionar_empresa'),
    path('adicionar_empresa/', adicionar_empresa, name='adicionar_empresa'),
    path('deletar_empresa/<int:id>', deletar_empresa, name='deletar_empresa'),
    path('editar/empresa/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    ## MODULO FUNCIONARIOS
    path('funcionarios/', funcionarios, name='funcionarios'),
    
]

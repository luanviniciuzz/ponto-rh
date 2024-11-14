from django.test import TestCase, Client
from django.urls import reverse
from sistema.models import Funcionario, Empresa, Ponto
import json

class TestViews(TestCase):
    def test_empresa_list_GET(self):
        client = Client()
        response = client.get(reverse('empresas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'empresas.html')

    def test_pagina_adicionar_empresa_GET(self):
        client = Client()
        response = client.get(reverse('pagina_adicionar_empresa'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_empresa.html')

    # def test_adicionar_empresa_POST(self):
    #     Empresa.objects.create(
    #         nome = "nome",
    #         endereco = "endereco",
    #         telefone = "33333333"
    #     )

        # client = Client()
        # response = client.post(reverse('adicionar_empresa'), {
        #    'nome' = 'nome',
        #    'endereco' = 'endereco',
        #    'telefone' = '33333333'
        # })
        # self.assertEqual(response.status_code, 302)


#  path('', index, name='mysite'),
# ## MODULO EMPRESAS
# path('empresas/', empresas, name='empresas'),
# path('empresas/adicionar/', pagina_adicionar_empresa, name='pagina_adicionar_empresa'),
# path('adicionar_empresa/', adicionar_empresa, name='adicionar_empresa'),
# path('deletar_empresa/<int:id>', deletar_empresa, name='deletar_empresa'),
# path('editar/empresa/<int:id>', editar_empresa, name='editar_empresa'),
# path('update/empresa/<int:id>', update_empresa, name='update_empresa'),
# ## MODULO FUNCIONARIOS
# path('funcionarios/', funcionarios, name='funcionarios'),
# path('funcionario/adicionar/', pagina_adicionar_funcionario, name='pagina_adicionar_funcionario'),
# path('adicionar_funcionario/', adicionar_funcionario, name='adicionar_funcionario'),
# path('deletar_funcionario/<int:id>', deletar_funcionario, name='deletar_funcionario'),
# path('editar/funcionario/<int:id>', editar_funcionario, name='editar_funcionario'),
# path('update/funcionario/<int:id>', update_funcionario, name='update_funcionario'),
# ## MODULO PONTO
# path('ponto/', ponto, name='ponto'),
# path('ponto/adicionar/', pagina_adicionar_ponto, name='pagina_adicionar_ponto'),
# path('adicionar_ponto/', adicionar_ponto, name='adicionar_ponto'),
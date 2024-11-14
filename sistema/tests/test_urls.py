from django.test import SimpleTestCase
from django.urls import reverse, resolve

from sistema.views import (
    index, adicionar_empresa, empresas, pagina_adicionar_empresa, deletar_empresa, editar_empresa, update_empresa,
    funcionarios, pagina_adicionar_funcionario, adicionar_funcionario, deletar_funcionario, update_funcionario, editar_funcionario,
    ponto, pagina_adicionar_ponto, adicionar_ponto
)

class TestUrls(SimpleTestCase):
    # Teste unitário para assegurar que a URL corresponde a função correta
    ## TESTE DA URL BASE
    def test_url_site_base(self):
        url = reverse('mysite')
        self.assertEqual(resolve(url).func, index)

    ## MODULO EMPRESAS
    def test_url_list_empresas(self):
        url = reverse('empresas')
        self.assertEqual(resolve(url).func, empresas)

    def test_url_pagina_adicionar_empresa(self):
        url = reverse('pagina_adicionar_empresa')
        self.assertEqual(resolve(url).func, pagina_adicionar_empresa)

    def test_url_adicionar_empresa(self):
        url = reverse('adicionar_empresa')
        self.assertEqual(resolve(url).func, adicionar_empresa)

    def test_url_deletar_empresa(self):
        url = reverse('deletar_empresa', kwargs={'id': 1})
        self.assertEqual(resolve(url).func, deletar_empresa)

    def test_url_editar_empresa(self):
        url = reverse('editar_empresa', kwargs={'id': 1})
        self.assertEqual(resolve(url).func, editar_empresa)

    def test_url_update_empresa(self):
        url = reverse('update_empresa', kwargs={'id': 1})
        self.assertEqual(resolve(url).func, update_empresa)

    ## MODULO FUNCIONARIOS
    def test_url_list_funcionarios(self):
        url = reverse('funcionarios')
        self.assertEqual(resolve(url).func, funcionarios)

    def test_url_pagina_adicionar_funcionario(self):
        url = reverse('pagina_adicionar_funcionario')
        self.assertEqual(resolve(url).func, pagina_adicionar_funcionario)

    def test_url_adicionar_funcionario(self):
        url = reverse('adicionar_funcionario')
        self.assertEqual(resolve(url).func, adicionar_funcionario)

    def test_url_deletar_funcionario(self):
        url = reverse('deletar_funcionario', kwargs={'id': 1})
        self.assertEqual(resolve(url).func, deletar_funcionario)

    def test_url_editar_funcionario(self):
        url = reverse('editar_funcionario', kwargs={'id': 1})
        self.assertEqual(resolve(url).func, editar_funcionario)

    def test_url_update_funcionario(self):
        url = reverse('update_funcionario', kwargs={'id': 1})
        self.assertEqual(resolve(url).func, update_funcionario)

    ## MODULO PONTO
    def test_url_list_ponto(self):
        url = reverse('ponto')
        self.assertEqual(resolve(url).func, ponto)

    def test_url_pagina_adicionar_ponto(self):
        url = reverse('pagina_adicionar_ponto')
        self.assertEqual(resolve(url).func, pagina_adicionar_ponto)

    def test_url_adicionar_ponto(self):
        url = reverse('adicionar_ponto')
        self.assertEqual(resolve(url).func, adicionar_ponto)
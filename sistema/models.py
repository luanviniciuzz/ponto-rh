from django.db import models

# class Empresa(models.Model):
#     nome = models.CharField(max_length=255)
#     endereco = models.CharField(max_length=255, blank=False)
#     telefone = models.CharField(max_length=14, blank=False)

#     def __str__(self):
#         return self.nome

# class Funcionario(models.Model):
#     nome = models.CharField(max_length=255, blank=False)
#     email = models.EmailField(max_length=255, blank=False, unique=True)
#     empresa = models.ForeignKey(Empresa , blank=False, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nome

# class Ponto(models.Model):
#     funcionario = models.ForeignKey(Funcionario, blank=False, on_delete=models.CASCADE)
#     entrada = models.DateTimeField(blank=False)
#     saida = models.DateTimeField(blank=False)

#     def __str__(self):
#         return self.entrada
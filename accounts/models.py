from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=[('funcionario', 'Funcionário'), ('empregador', 'Empregador')])
    
    def __str__(self):
        return self.get_role_display()

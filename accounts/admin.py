from django.contrib.auth.models import User
from django.contrib.auth import forms
from django import forms as django_forms
from .models import CustomUser
from django.contrib import admin

admin.site.register(CustomUser)
# Register your models here.
class CustomUserCreationForm(forms.UserCreationForm):
    ROLE_CHOICES = [
        ('funcionario', 'Funcionário'),
        ('empregador', 'Empregador'),
    ]
    
    role = django_forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Tipo de Usuário")

    class Meta(forms.UserCreationForm.Meta):
        model = CustomUser
        fields = forms.UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'role')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Criar o Profile associado e definir o role
            role = self.cleaned_data.get('role')
            CustomUser.objects.create(user=user, role=role)
        return user
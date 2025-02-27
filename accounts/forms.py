from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser
import re
from django.core.exceptions import ValidationError

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'exemplo@email.com'})
    )


    error_messages = {
        'invalid_login': "Credenciais inválidas",
        'inactive': "Esta conta está inativa",
    }

class RegistroForm(UserCreationForm):
    nome_completo = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nome completo'}),
        help_text="Somente letras e espaços"
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail'})
    )

    class Meta:
        model = CustomUser
        fields = ["nome_completo", "email", "password1", "password2"]

def clean_nome_completo(self):
    nome = self.cleaned_data.get('nome_completo')
    # Regex corrigida:
    if not re.match(r'^[a-zA-ZÀ-ÿ\s]+$', nome):
        raise ValidationError("O nome deve conter apenas letras e espaços.")
    return nome  # Certifique-se de retornar o nome!
def clean_email(self):
    email = self.cleaned_data.get('email').lower()
    if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está cadastrado.")
    return email
def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        # Validação detalhada da senha
        if len(password1) < 8:
            raise ValidationError("Mínimo 8 caracteres.")
        if not re.search(r'[A-Z]', password1):
            raise ValidationError("Pelo menos 1 letra maiúscula.")
        if not re.search(r'[0-9]', password1):
            raise ValidationError("Pelo menos 1 número.")
        if not re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password1):
            raise ValidationError("Pelo menos 1 caractere especial.")
        return password1

def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "As senhas não coincidem!")
        return cleaned_data

def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"].lower()  # Normaliza e-mail
        user.nome_completo = self.cleaned_data["nome_completo"].strip()
        if commit:
            user.save()
        return user
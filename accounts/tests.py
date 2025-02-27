# accounts/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

class LoginTestCase(TestCase):
    def setUp(self):
        """Configuração inicial do teste"""
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            nome_completo='Teste',
            password='Senha123@'
        )

    def test_login_valido(self):
        """Teste de login com credenciais corretas"""
        response = self.client.post(reverse('login'), {
            'email': 'test@example.com',  # O campo correto é 'email', não 'username'
            'password': 'Senha123@'
        })
        self.assertRedirects(response, reverse('menu'))  # Melhor usar reverse para evitar erros de rota

class RegistroTestCase(TestCase):
    def setUp(self):
        """Configuração inicial do teste"""
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            nome_completo='Teste',
            password='Senha123@'
        )

    def test_registro_email_duplicado(self):
        """Teste de erro ao tentar registrar um e-mail já existente"""
        response = self.client.post(reverse('registro'), {
            'nome_completo': 'Teste2',
            'email': 'test@example.com',
            'password1': 'Senha123@',
            'password2': 'Senha123@'
        })

        self.assertFormError(response, 'form', 'email', 'Este e-mail já está cadastrado.')

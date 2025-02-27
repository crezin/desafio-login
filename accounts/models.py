# ------------------------------- #
#           models.py             #
# ------------------------------- #
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """
    Modelo de usuário personalizado que substitui o usuário padrão do Django
    Herda de AbstractUser e adiciona campos personalizados
    """
    # Remover o campo username padrão
    username = None
    
    # Campo email como identificador único
    email = models.EmailField(
        _('Endereço de email'),
        unique=True,
        help_text='Endereço de e-mail único para identificação do usuário'
    )
    
    # Campo nome completo
    nome_completo = models.CharField(
        _('Nome completo'),
        max_length=150,
        help_text='Nome completo do usuário'
    )

    # Data de criação da conta
    date_joined = models.DateTimeField(auto_now_add=True)

    # Configurações de autenticação
    USERNAME_FIELD = 'email'  # Campo usado para login
    REQUIRED_FIELDS = ['nome_completo']  # Campos obrigatórios ao criar superusuário

    def __str__(self):
        """Representação em string do usuário"""
        return f"{self.nome_completo} <{self.email}>"

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-date_joined']
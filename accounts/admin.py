# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Configuração do list_display
    list_display = ('email', 'get_name', 'is_staff', 'is_active')
    
    # Campos para edição rápida
    list_editable = ('is_active',)
    
    # Filtros
    list_filter = ('is_staff', 'is_active')
    
    # Campos de busca
    search_fields = ('email', 'name')
    
    # Ordenação padrão
    ordering = ('email',)
    
    # Método para exibir o nome
    def get_name(self, obj):
        return obj.name
    get_name.short_description = 'Nome'  # Nome da coluna no admin
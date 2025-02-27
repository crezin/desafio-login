# ------------------------------- #
#           views.py              #
# ------------------------------- #
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import LoginForm, RegistroForm
from django.contrib.auth.decorators import login_required
def login_view(request):
    """
    View para tratamento do login de usuários
    """
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            # Autenticação do usuário
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.nome_completo}!")
            return redirect('menu')
        else:
            # Tratamento de erros
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def registro_view(request):
    """
    View para registro de novos usuários
    """
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        
        if form.is_valid():
            # Salvar usuário e enviar email
            user = form.save()
            site_url = getattr(settings, 'SITE_URL', 'http://localhost:8000')
            # Envio de email de confirmação
            send_mail(
                'Cadastro Confirmado - Fidelity',
                f'''Parabéns {user.nome_completo},\n\n
                Seu cadastro foi realizado com sucesso!\n
                Acesse o sistema: {settings.SITE_URL}/login\n\n
                Atenciosamente,\nEquipe Fidelity''',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            
            # Login automático após registro
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('menu')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

def logout_view(request):
    """View para logout de usuários"""
    logout(request)
    messages.success(request, "Você foi desconectado com sucesso!")
    return redirect('login')

def registro_sucesso(request):
    """Página de confirmação de registro"""
    return render(request, 'registro_sucesso.html')

def menu_view(request):
    """Página principal após login"""
    return render(request, 'menu.html')
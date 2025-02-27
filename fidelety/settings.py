"""
Django settings for fidelety project.
"""

from pathlib import Path
import os

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = 'django-insecure-f)%3p82%$3gnd6d5^fhn#rmfcd32x4wt=c*ojj#%%)25$6#&q3'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fidelety.urls'

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'accounts/'],  # Caminho absoluto
        'APP_DIRS': True,  # Habilita busca de templates nos apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fidelety.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'accounts/static']

# Custom User Model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Authentication
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'menu'
LOGOUT_REDIRECT_URL = 'login'

# Email Configuration (Para o extra)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'f75187744@gmail.com'  # Configure com seus dados
EMAIL_HOST_PASSWORD = 'aoce gwry lars pdxp'    # Use variáveis de ambiente na produção
DEFAULT_FROM_EMAIL = 'f75187744@gmail.com'
# Security (Desative em desenvolvimento)
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# settings.py
SESSION_COOKIE_AGE = 3600  # 1 hora de sessão
# settings.py
SITE_URL = 'http://localhost:8000'  # URL base do seu site (desenvolvimento)
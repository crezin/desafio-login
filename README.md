# Desafio Técnico Fidelity Pesquisas - Sistema de Autenticação

[![Django](https://img.shields.io/badge/Django-4.2.8-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)

Sistema de autenticação desenvolvido em Django para o processo seletivo da Fidelity Pesquisas Cadastrais, contendo:

- 🚀 Tela de Login com validações
- 📝 Tela de Registro com critérios de segurança
- ✉️ Envio de e-mail de confirmação (funcionalidade extra)
- 📊 Banco de dados SQLite

## Pré-requisitos

- Python 3.10+
- Pip
- Git

## 🛠 Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/desafio-login.git
cd desafio-login

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute as migrações
python manage.py migrate

# 5. Crie um superusuário (opcional)
python manage.py createsuperuser

```
### Como Executar

Para iniciar o servidor, use o seguinte comando no terminal:

```bash
python manage.py runserve
```

✅ **Funcionalidades Implementadas**

**Tela de Login**
- Validação de campos obrigatórios

**Mensagens de erro específicas:**
- 🔴 E-mail inexistente
- 🔴 Senha inválida
- 🔴 Credenciais incorretas

- Redirecionamento para Menu após login

**Tela de Registro**
- Validações em tempo real:
  - 🔠 Nome: Apenas letras e espaços
  - 📧 E-mail: Formato válido com @
  - 🔒 Senha:
    - 8+ caracteres
    - 1 letra maiúscula
    - 1 número
    - 1 caractere especial
  - 🔄 Confirmação de senha idêntica
  - Toggle para visualização de senha 👁️
  - Envio automático de e-mail de confirmação (opcional)

**🧪 Testes**
- Testes automatizados incluídos para:
  - Registro com e-mail duplicado
  - Validação de critérios de senha
  - Fluxo de login válido

**📄 Estrutura do Projeto**

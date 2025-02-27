// scripts.js
function togglePassword(fieldId, iconId) {
    const passwordField = document.getElementById(fieldId);
    const iconElement = document.getElementById(iconId);
    
    if (!passwordField || !iconElement) {
        console.error('Elementos não encontrados:', {fieldId, iconId});
        return;
    }

    const isPassword = passwordField.type === 'password';
    passwordField.type = isPassword ? 'text' : 'password';
    
    try {
        iconElement.classList.toggle('fa-eye-slash', !isPassword);
        iconElement.classList.toggle('fa-eye', isPassword);
    } catch (error) {
        console.error('Erro ao alternar classes:', error);
    }
}

function initLoginPasswordToggle() {
    const toggleBtn = document.getElementById('toggle-password');
    if (!toggleBtn) return;

    toggleBtn.addEventListener('click', (e) => {
        e.preventDefault();
        togglePassword('password1-field', 'toggle-password');
        toggleBtn.animate([
            { transform: 'scale(1)' },
            { transform: 'scale(1.1)' },
            { transform: 'scale(1)' }
        ], { duration: 200 });
    });
}

function toggleBothPasswords() {
    const mainIcon = document.getElementById('toggle-password');
    if (!mainIcon) return;
    
    togglePassword('password1-field', 'toggle-password');
    togglePassword('password2-field', 'toggle-password');
    
    mainIcon.animate([
        { transform: 'scale(1)' },
        { transform: 'scale(1.2)' },
        { transform: 'scale(1)' }
    ], { duration: 300 });
}

function initInputEffects() {
    const inputFields = document.querySelectorAll('.input-field');
    inputFields.forEach(input => {
        input.addEventListener('mouseenter', () => {
            input.style.boxShadow = '0 0 20px var(--green-primary), 0 0 40px var(--green-glow)';
            if (input.parentElement) {
                input.parentElement.style.transform = 'scale(1.02)';
            }
        });

        input.addEventListener('mouseleave', () => {
            input.style.boxShadow = '0 0 10px var(--green-glow)';
            if (input.parentElement) {
                input.parentElement.style.transform = 'scale(1)';
            }
        });

        input.addEventListener('focus', () => {
            input.style.transform = 'scale(1.02)';
            input.style.letterSpacing = '1.5px';
        });

        input.addEventListener('blur', () => {
            input.style.transform = 'scale(1)';
            input.style.letterSpacing = '0.5px';
        });
    });
}

document.addEventListener('DOMContentLoaded', () => {
    // Alternar senha do Login
    const togglePassword = document.getElementById('toggle-password');
    const passwordField = document.getElementById('id_password');

    if (togglePassword && passwordField) {
        togglePassword.addEventListener('click', () => {
            const isPassword = passwordField.type === 'password';
            passwordField.type = isPassword ? 'text' : 'password';
            togglePassword.classList.toggle('fa-eye-slash', isPassword);
            togglePassword.classList.toggle('fa-eye', !isPassword);
        });
    }

    // Alternar senha no Registro (senha e confirmar senha)
    const togglePasswords = document.getElementById('toggle-passwords');
    const password1 = document.getElementById('password1');
    const password2 = document.getElementById('password2');

    if (togglePasswords && password1 && password2) {
        togglePasswords.addEventListener('click', () => {
            const isPassword = password1.type === 'password';

            password1.type = isPassword ? 'text' : 'password';
            password2.type = isPassword ? 'text' : 'password';

            togglePasswords.classList.toggle('fa-eye-slash', isPassword);
            togglePasswords.classList.toggle('fa-eye', !isPassword);
        });
    }
});

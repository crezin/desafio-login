from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView  # Importação correta
from accounts import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('menu/', views.menu_view, name='menu'),
    path('logout/', views.logout_view, name='logout'),
    path('registro-sucesso/', views.registro_sucesso, name='registro_sucesso'),
    path('', RedirectView.as_view(url='/login/')),  # Redirecionamento raiz

      path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        success_url='/password-reset/done/'
    ), name='password_reset'),
    
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]
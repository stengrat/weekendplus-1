from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('registrar/', views.paginaRegistro, name='registrar'),
    path('login/', views.paginaLogin, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('obrigado/', views.paginaObrigado, name='obrigado'),
    path('dashboard_perfil/', views.userDashboardPerfil, name='dashboard'),
    path('dashboard_conta/', views.userDashboardConta, name='dashboard_conta'),

    # Rotas para reset de senha
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='contas/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='contas/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='contas/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='contas/password_reset_done.html'), name='password_reset_complete'),

    #Rotas para confirmação da conta
    path('activate/<uidb64>/<token>/', views.ativacaoConta, name='activate'),

]
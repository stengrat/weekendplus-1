from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.paginaRegistro, name='registrar'),
    path('login/', views.paginaLogin, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('obrigado/', views.paginaObrigado, name='obrigado'),
    path('dashboard/', views.userDashboard, name='dashboard')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaInicial, name='home'),
    path('404/', views.error_404, name='404')

]
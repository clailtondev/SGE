# sge/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pessoas, name='lista_pessoas'),
    path('novo/', views.criar_pessoa, name='criar_pessoa'),
    path('alterar/<int:id_pessoa>/', views.alterar_pessoa, name='alterar_pessoa'),
    path('excluir/<int:id_pessoa>/', views.excluir_pessoa, name='excluir_pessoa'),
]
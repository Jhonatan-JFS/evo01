from django.urls import path;
from . import views;

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('projeto/<int:id>/', views.detalhe, name='detalhe'),
]
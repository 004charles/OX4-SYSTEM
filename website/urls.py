from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    # Páginas principais
    path('', views.homesite, name='homesite'),
    path('homesite/', views.homesite, name='homesite'),
    path('sobresite/', views.sobresite, name='sobresite'),
    path('passageiro/', views.passageiro, name='passageiro'),
    path('motoqueiro/', views.motoqueiro, name='motoqueiro'),
    path('contacto/', views.mensagemcontacto, name='contacto'),
    path('servico/', views.servico, name='servico'),
    path('sucesso/', lambda request: render(request, 'sucesso.html'), name='sucesso'),
    
    path('servicos/<slug:slug>/', views.ServicoDetailView.as_view(), name='detalhe_servico'),
]
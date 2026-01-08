from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path('sucesso/', lambda request: render(request, 'sucesso.html'), name='sucesso'),
]


from . import views


urlpatterns = [
    path('homesite/', views.homesite, name = 'homesite'),
    path('sobresite/', views.sobresite, name = 'sobresite'),
    path('passageiro/', views.passageiro, name = 'passageiro'),
    path('motoqueiro/', views.motoqueiro, name = 'motoqueiro'),
    path('sobresite/', views.sobresite, name = 'sobresite'),
    path('contacto/', views.mensagemcontacto, name='contacto'),
    path('servico/', views.servico, name = 'servico')
    
]


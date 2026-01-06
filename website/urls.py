from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('homesite/', views.homesite, name = 'homesite'),
    path('sobresite/', views.sobresite, name = 'sobresite'),
    path('passageiro/', views.passageiro, name = 'passageiro'),
    path('motoqueiro/', views.motoqueiro, name = 'motoqueiro'),
    path('sobresite/', views.sobresite, name = 'sobresite')
    
]


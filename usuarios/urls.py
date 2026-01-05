from django.urls import path
from .views import (
    PerfilUsuarioView,
    RegistroClienteView,
    RegistroMototaxistaView,
    MotoCreateListView
)

urlpatterns = [
    path('perfil/', PerfilUsuarioView.as_view(), name='perfil-usuario'),
    path('registrar/cliente/', RegistroClienteView.as_view(), name='registrar-cliente'),
    path('registrar/mototaxista/', RegistroMototaxistaView.as_view(), name='registrar-mototaxista'),
    path('motos/', MotoCreateListView.as_view(), name='motos'),
]

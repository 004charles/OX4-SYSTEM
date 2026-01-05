from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_admin, name="login_admin"),
    path("logout/", views.logout_admin, name="logout_admin"),
    path("painel/", views.painel_admin, name="painel_admin"),
    path("clientes/", views.clientes_admin, name="clientes_admin"),
    path("mototaxistas/", views.mototaxistas_admin, name="mototaxistas_admin"),
    path("motos/", views.motos_admin, name="motos_admin"),
    path("corridas/", views.corridas_admin, name="corridas_admin"),
]

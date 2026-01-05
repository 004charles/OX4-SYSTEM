from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from usuarios.models import Cliente, Mototaxista, Moto, Corrida

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from usuarios.models import Cliente, Mototaxista, Moto, Corrida, Usuario  # <- modelo customizado

# Verifica se o usuário é admin
def is_admin(user):
    return user.is_staff

# Login do admin com status detalhado para modelo customizado
def login_admin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Verifica se o usuário existe no modelo customizado
        try:
            user_obj = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")
            return redirect("login_admin")

        # Autentica o usuário
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}!")
            return redirect("painel_admin")
        else:
            messages.error(request, "Senha incorreta ou você não tem permissão de admin.")
            return redirect("login_admin")

    return render(request, "loginadmin.html")

# Logout do admin
@login_required
def logout_admin(request):
    logout(request)
    return redirect("login_admin")

# Painel principal
@login_required
@user_passes_test(is_admin)
def painel_admin(request):
    return render(request, "paineladmin.html")

# Listar clientes
@login_required
@user_passes_test(is_admin)
def clientes_admin(request):
    clientes = Cliente.objects.all()
    return render(request, "adminpanel/clientes.html", {"clientes": clientes})

# Listar mototaxistas
@login_required
@user_passes_test(is_admin)
def mototaxistas_admin(request):
    mototaxistas = Mototaxista.objects.all()
    return render(request, "adminpanel/mototaxistas.html", {"mototaxistas": mototaxistas})

# Listar motos
@login_required
@user_passes_test(is_admin)
def motos_admin(request):
    motos = Moto.objects.all()
    return render(request, "adminpanel/motos.html", {"motos": motos})

# Listar corridas
@login_required
@user_passes_test(is_admin)
def corridas_admin(request):
    corridas = Corrida.objects.all()
    return render(request, "adminpanel/corridas.html", {"corridas": corridas})

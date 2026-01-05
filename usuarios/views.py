from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Usuario, Moto, Corrida, Avaliacao
from .serializers import (
    UsuarioSerializer,
    RegistroClienteSerializer,
    RegistroMototaxistaSerializer,
    MotoSerializer,
    CorridaSerializer,
    AvaliacaoSerializer
)

# -----------------------------
# PERFIL DO USUÁRIO
# -----------------------------
class PerfilUsuarioView(generics.RetrieveAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# -----------------------------
# REGISTRO CLIENTE
# -----------------------------
class RegistroClienteView(generics.CreateAPIView):
    serializer_class = RegistroClienteSerializer
    permission_classes = [permissions.AllowAny]

# -----------------------------
# REGISTRO MOTOTAXISTA
# -----------------------------
class RegistroMototaxistaView(generics.CreateAPIView):
    serializer_class = RegistroMototaxistaSerializer
    permission_classes = [permissions.AllowAny]

# -----------------------------
# LISTA E CRIAÇÃO DE MOTOS
# -----------------------------
class MotoCreateListView(generics.ListCreateAPIView):
    serializer_class = MotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Moto.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Apenas administradores podem cadastrar motos.")
        serializer.save()

# -----------------------------
# LISTA E CRIAÇÃO DE CORRIDAS
# -----------------------------
class CorridaCreateListView(generics.ListCreateAPIView):
    serializer_class = CorridaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'cliente'):
            return Corrida.objects.filter(cliente=user.cliente)
        elif hasattr(user, 'mototaxista'):
            return Corrida.objects.filter(mototaxista=user.mototaxista)
        return Corrida.objects.none()

    def perform_create(self, serializer):
        if not hasattr(self.request.user, 'cliente'):
            raise PermissionDenied("Apenas clientes podem solicitar corridas.")
        serializer.save(cliente=self.request.user.cliente)

# -----------------------------
# LISTA E CRIAÇÃO DE AVALIACOES
# -----------------------------
class AvaliacaoCreateListView(generics.ListCreateAPIView):
    serializer_class = AvaliacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'cliente'):
            return Avaliacao.objects.filter(corrida__cliente=user.cliente)
        elif hasattr(user, 'mototaxista'):
            return Avaliacao.objects.filter(corrida__mototaxista=user.mototaxista)
        return Avaliacao.objects.none()

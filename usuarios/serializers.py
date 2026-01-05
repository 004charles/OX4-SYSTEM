from rest_framework import serializers
from .models import Usuario, Cliente, Mototaxista, Moto, Corrida, Avaliacao, PerfilMototaxista
from django.contrib.auth.password_validation import validate_password

# -----------------------------
# USUARIO
# -----------------------------
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'tipo')

# -----------------------------
# REGISTRO CLIENTE
# -----------------------------
class RegistroClienteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    telefone = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'telefone')

    def create(self, validated_data):
        telefone = validated_data.pop('telefone')
        usuario = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            tipo='CLIENTE'
        )
        # Atualiza telefone do perfil criado pelo signal
        usuario.cliente.telefone = telefone
        usuario.cliente.save()
        return usuario


class PerfilMototaxistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilMototaxista
        fields = '__all__'

# -----------------------------
# REGISTRO MOTOTAXISTA
# -----------------------------
class RegistroMototaxistaSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    telefone = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'telefone')

    def create(self, validated_data):
        telefone = validated_data.pop('telefone')
        usuario = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            tipo='MOTOTAXISTA'
        )
        usuario.mototaxista.telefone = telefone
        usuario.mototaxista.save()
        return usuario

# -----------------------------
# MOTO
# -----------------------------
class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'

# -----------------------------
# CORRIDA
# -----------------------------
class CorridaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corrida
        fields = '__all__'

# -----------------------------
# AVALIACAO
# -----------------------------
class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'

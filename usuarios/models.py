from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from core.models import BaseModel


# -----------------------------
# USUÁRIO
# -----------------------------
class Usuario(AbstractUser):

    TIPO_USUARIO = (
        ('CLIENTE', 'Cliente'),
        ('MOTOTAXISTA', 'Mototaxista'),
    )

    tipo = models.CharField(max_length=15, choices=TIPO_USUARIO)

    def clean(self):
        if self.tipo not in ['CLIENTE', 'MOTOTAXISTA']:
            raise ValidationError("Tipo de usuário inválido.")

    def __str__(self):
        return f"{self.username} ({self.tipo})"


# -----------------------------
# CLIENTE
# -----------------------------
class Cliente(BaseModel):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, related_name='cliente'
    )
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Cliente - {self.usuario.username}"



class PerfilCliente(BaseModel):
    cliente = models.OneToOneField(
        'Cliente', on_delete=models.CASCADE, related_name='perfil'
    )
    
    # Dados de contato
    telefone_alternativo = models.CharField(max_length=20, null=True, blank=True)
    email_alternativo = models.EmailField(null=True, blank=True)
    
    # Preferências
    idioma_preferido = models.CharField(max_length=10, default='pt', choices=[
        ('pt', 'Português'),
        ('en', 'Inglês'),
        ('fr', 'Francês'),
    ])
    
    # Métodos de pagamento preferidos
    metodo_pagamento_preferido = models.CharField(max_length=20, default='DINHEIRO', choices=[
        ('DINHEIRO', 'Dinheiro'),
        ('MBWAY', 'MBWay'),
        ('CARTAO', 'Cartão'),
        ('TRANSFERENCIA', 'Transferência'),
    ])
    
    # Histórico e estatísticas
    total_corridas = models.PositiveIntegerField(default=0)
    total_gasto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    membro_desde = models.DateTimeField(auto_now_add=True)
    
    # Localizações frequentes (endereços favoritos)
    casa_endereco = models.CharField(max_length=200, null=True, blank=True)
    trabalho_endereco = models.CharField(max_length=200, null=True, blank=True)
    
    # Configurações de notificação
    receber_notificacoes_push = models.BooleanField(default=True)
    receber_promocoes_email = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Perfil de {self.cliente.usuario.username}"


# -----------------------------
# MOTOTAXISTA
# -----------------------------
class Mototaxista(BaseModel):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, related_name='mototaxista'
    )
    telefone = models.CharField(max_length=20)
    verificado = models.BooleanField(default=False)
    disponivel = models.BooleanField(default=False)

    def __str__(self):
        return f"Mototaxista - {self.usuario.username}"



class PerfilMototaxista(BaseModel):
    mototaxista = models.OneToOneField(
        'Mototaxista', on_delete=models.CASCADE, related_name='perfil'
    )
    
    # Dados pessoais
    bi_numero = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name="Número do BI")
    bi_frente = models.ImageField(upload_to='documentos/bi/frente/', null=True, blank=True)
    bi_verso = models.ImageField(upload_to='documentos/bi/verso/', null=True, blank=True)
    
    # Documentação da moto (caso não tenha modelo Moto separado)
    carta_conducao_numero = models.CharField(max_length=50, null=True, blank=True)
    carta_conducao_validade = models.DateField(null=True, blank=True)
    carta_conducao_foto = models.ImageField(upload_to='documentos/carta_conducao/', null=True, blank=True)
    
    # Avaliação geral
    classificacao_media = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_corridas = models.PositiveIntegerField(default=0)
    total_avaliacoes = models.PositiveIntegerField(default=0)
    
    # Informações bancárias para pagamentos
    banco_nome = models.CharField(max_length=100, null=True, blank=True)
    iban = models.CharField(max_length=34, null=True, blank=True)
    conta_numero = models.CharField(max_length=50, null=True, blank=True)
    
    # Localização atual (para corridas)
    ultima_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    ultima_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    ultima_atualizacao_localizacao = models.DateTimeField(null=True, blank=True)
    
    # Configurações
    aceita_corridas_longas = models.BooleanField(default=True)
    raio_atendimento_km = models.PositiveIntegerField(default=10, help_text="Raio máximo em km para aceitar corridas")
    
    def __str__(self):
        return f"Perfil de {self.mototaxista.usuario.username}"


# -----------------------------
# MOTO
# -----------------------------
class Moto(BaseModel):
    mototaxista = models.ForeignKey(
        Mototaxista, on_delete=models.CASCADE, related_name='motos'
    )
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=30)
    matricula = models.CharField(max_length=20, unique=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.matricula} - {self.marca} {self.modelo}"


# -----------------------------
# CORRIDA
# -----------------------------
class Corrida(BaseModel):
    STATUS = (
        ('PENDENTE', 'Pendente'),
        ('ACEITA', 'Aceita'),
        ('EM_CURSO', 'Em Curso'),
        ('FINALIZADA', 'Finalizada'),
        ('CANCELADA', 'Cancelada'),
    )

    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='corridas'
    )
    mototaxista = models.ForeignKey(
        Mototaxista, on_delete=models.SET_NULL, null=True, blank=True, related_name='corridas'
    )
    moto = models.ForeignKey(
        Moto, on_delete=models.SET_NULL, null=True, blank=True, related_name='corridas'
    )
    origem = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS, default='PENDENTE')
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    distancia_km = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Corrida {self.id} - {self.cliente.usuario.username} ({self.status})"


# -----------------------------
# AVALIACAO
# -----------------------------
class Avaliacao(BaseModel):
    corrida = models.OneToOneField(
        Corrida, on_delete=models.CASCADE, related_name='avaliacao'
    )
    nota = models.PositiveIntegerField()
    comentario = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Avaliação Corrida {self.corrida.id} - Nota: {self.nota}"


# -----------------------------
# SIGNALS PARA PERFIS AUTOMÁTICOS
# -----------------------------
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Usuario)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        if instance.tipo == 'CLIENTE':
            Cliente.objects.create(usuario=instance)
        elif instance.tipo == 'MOTOTAXISTA':
            Mototaxista.objects.create(usuario=instance)

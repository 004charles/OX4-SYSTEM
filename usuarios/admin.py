from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Cliente, Mototaxista, Moto, Corrida, Avaliacao

# -----------------------------
# INLINES
# -----------------------------
class ClienteInline(admin.StackedInline):
    model = Cliente
    extra = 0
    can_delete = False
    verbose_name = "Perfil de Cliente"
    verbose_name_plural = "Perfil de Cliente"

class MototaxistaInline(admin.StackedInline):
    model = Mototaxista
    extra = 0
    can_delete = False
    verbose_name = "Perfil de Mototaxista"
    verbose_name_plural = "Perfil de Mototaxista"

# -----------------------------
# ADMIN DO USUARIO
# -----------------------------
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'tipo', 'is_staff', 'is_active')
    list_filter = ('tipo', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    inlines = [ClienteInline, MototaxistaInline]

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('email', 'tipo')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

# -----------------------------
# ADMIN CLIENTE
# -----------------------------
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefone', 'ativo', 'criado_em')
    search_fields = ('usuario__username', 'telefone')
    list_filter = ('ativo',)

# -----------------------------
# ADMIN MOTOTAXISTA
# -----------------------------
@admin.register(Mototaxista)
class MototaxistaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefone', 'verificado', 'disponivel', 'criado_em')
    search_fields = ('usuario__username', 'telefone')
    list_filter = ('verificado', 'disponivel')

# -----------------------------
# ADMIN MOTO
# -----------------------------
@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'cor', 'matricula', 'ativa', 'mototaxista')
    search_fields = ('marca', 'modelo', 'matricula', 'cor')
    list_filter = ('ativa', 'marca')

# -----------------------------
# ADMIN CORRIDA
# -----------------------------
@admin.register(Corrida)
class CorridaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'mototaxista', 'status', 'preco', 'criado_em')
    search_fields = ('cliente__usuario__username', 'mototaxista__usuario__username')
    list_filter = ('status',)

# -----------------------------
# ADMIN AVALIACAO
# -----------------------------
@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('corrida', 'nota')
    search_fields = ('corrida__cliente__usuario__username', 'corrida__mototaxista__usuario__username')

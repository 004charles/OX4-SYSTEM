from django.contrib import admin
from .models import MensagemContacto


@admin.register(MensagemContacto)
class MensagemContactoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'criado_em')
    search_fields = ('nome', 'email', 'assunto')

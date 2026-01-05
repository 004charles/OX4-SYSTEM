from django.contrib import admin
from .models import LogAdministrativo


@admin.register(LogAdministrativo)
class LogAdministrativoAdmin(admin.ModelAdmin):
    list_display = ('administrador', 'acao', 'criado_em')
    search_fields = ('administrador__username', 'acao')

from django.contrib import admin
from .models import Servico, BeneficioServico

class BeneficioServicoInline(admin.TabularInline):
    model = BeneficioServico
    extra = 1

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'ativo', 'ordem', 'data_criacao')
    list_filter = ('categoria', 'ativo')
    search_fields = ('titulo', 'descricao_curta', 'descricao_longa')
    prepopulated_fields = {'slug': ('titulo',)}
    inlines = [BeneficioServicoInline]
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'subtitulo', 'slug', 'categoria', 'icone', 'ordem', 'ativo')
        }),
        ('Conteúdo', {
            'fields': ('imagem_principal', 'imagem_secundaria', 'descricao_curta', 
                      'descricao_longa', 'caracteristicas')
        }),
        ('SEO', {
            'fields': ('meta_titulo', 'meta_descricao'),
            'classes': ('collapse',)
        }),
    )

@admin.register(BeneficioServico)
class BeneficioServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'servico', 'ordem')
    list_filter = ('servico',)
    search_fields = ('titulo', 'descricao')
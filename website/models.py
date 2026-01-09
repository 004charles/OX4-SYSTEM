from django.db import models
from core.models import BaseModel


class MensagemContacto(BaseModel):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome



from django.db import models
from django.utils.text import slugify

class Servico(models.Model):
    CATEGORIA_CHOICES = [
        ('moto_taxi', 'Moto Táxi'),
        ('moto_entrega', 'Moto Entrega'),
    ]
    
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    icone = models.CharField(max_length=50, default='fa-motorcycle')
    imagem_principal = models.ImageField(upload_to='servicos/', null=True, blank=True)
    imagem_secundaria = models.ImageField(upload_to='servicos/', null=True, blank=True)
    
    descricao_curta = models.TextField()
    descricao_longa = models.TextField()  # Mudado de RichTextField para TextField
    
    caracteristicas = models.TextField(help_text="Separe cada característica com vírgula", blank=True)
    
    ativo = models.BooleanField(default=True)
    ordem = models.IntegerField(default=0)
    
    meta_titulo = models.CharField(max_length=200, blank=True)
    meta_descricao = models.TextField(blank=True)
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['ordem', 'titulo']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        if not self.meta_titulo:
            self.meta_titulo = self.titulo
        if not self.meta_descricao:
            self.meta_descricao = self.descricao_curta[:160]
        super().save(*args, **kwargs)
    
    def get_caracteristicas_list(self):
        """Retorna lista de características"""
        if self.caracteristicas:
            return [caract.strip() for caract in self.caracteristicas.split(',')]
        return []
    
    def __str__(self):
        return self.titulo


class BeneficioServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='beneficios')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, default='fa-check')
    ordem = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['ordem']
    
    def __str__(self):
        return f"{self.servico.titulo} - {self.titulo}"
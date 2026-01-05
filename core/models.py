from django.db import models

# Create your models here.
from django.db import models

class BaseModel(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True




class StatusCorrida(models.TextChoices):
    SOLICITADA = 'SOLICITADA', 'Solicitada'
    ACEITA = 'ACEITA', 'Aceita'
    EM_ANDAMENTO = 'EM_ANDAMENTO', 'Em andamento'
    CONCLUIDA = 'CONCLUIDA', 'Concluída'
    CANCELADA = 'CANCELADA', 'Cancelada'




class StatusPagamento(models.TextChoices):
    PENDENTE = 'PENDENTE', 'Pendente'
    PAGO = 'PAGO', 'Pago'
    FALHOU = 'FALHOU', 'Falhou'
from django.db import models
from core.models import BaseModel


class MensagemContacto(BaseModel):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=150)
    mensagem = models.TextField()


    def __str__(self):
        return self.nome
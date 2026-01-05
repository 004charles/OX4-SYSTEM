from django.db import models
from core.models import BaseModel
from usuarios.models import Usuario


class LogAdministrativo(BaseModel):
    administrador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    acao = models.CharField(max_length=255)
    descricao = models.TextField()


    def __str__(self):
        return self.acao
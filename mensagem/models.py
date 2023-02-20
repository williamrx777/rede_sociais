from django.db import models
from django.contrib.auth.models import User

class Mensagem(models.Model):
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remetente')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinatario')
    texto = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)

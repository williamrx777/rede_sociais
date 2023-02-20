from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Conta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    foto = models.ImageField(upload_to='foto')

    def __str__(self):
        return self.texto

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    capa = models.ImageField(upload_to='capa')
    perfil = models.ImageField(upload_to='perfil')




class Batepapo(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    mensagem = models.TextField()
    imagem = models.ImageField(upload_to='imagem')

    def __str__(self):
        return self.mensagem



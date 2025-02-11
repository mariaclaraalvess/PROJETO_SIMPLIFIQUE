from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)

class Evento(models.Model):
    TIPOS_EVENTO = [
        ('reuniao', 'Reunião'),
        ('festa', 'Festa'),
        ('palestra', 'Palestra'),
    ]
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    horario_inicio = models.DateTimeField(default=timezone.now)
    local = models.CharField(max_length=255)
    tipo_evento = models.CharField(max_length=50, choices=TIPOS_EVENTO)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


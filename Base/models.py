from django.db import models
from django.contrib.auth.models import User

class Modelo(models.Model):
    titulo = models.CharField(max_length=100)
    diseño = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=500)
    fechaPost = models.DateField()
    emailUsuario = models.EmailField()

    def __str__(self):
        return f"{self.titulo} {self.diseño} {self.descripcion}"
    
class Comentario(models.Model):
    nombre = models.CharField(max_length=50)
    comentario = models.CharField(max_length=500)
    fechaComentario = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.comentario}"
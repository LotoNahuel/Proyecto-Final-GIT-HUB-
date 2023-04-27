from django.db import models
from django.contrib.auth.models import User

class Modelo(models.Model):
    diseñoSelect =(
    ('arte','Arte'),
    ('moda','Moda'),
    ('joya','Joya'),
    ('casa','Casa'),
    ('arquitectura','Arquitectura'),
    ('artilugio','Artilugio'),
    ('juego','Juego'),
    ('herramienta','Herramienta'),
    ('otro','Otro'),
    )
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="post", null=True)
    diseño = models.CharField(max_length=20, null=False, blank=False, choices=diseñoSelect)
    descripcion = models.CharField(max_length=500)
    fechaPost = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} {self.descripcion}"
    
class Comentario(models.Model):
    nombre = models.CharField(max_length=50)
    comentario = models.CharField(max_length=500)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.comentario}"
    
class Avatar(models.Model):
    image = models.ImageField(upload_to="avatar")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
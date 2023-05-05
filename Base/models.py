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
    imagen = models.ImageField(upload_to="post", null=True, blank=True)
    diseño = models.CharField(max_length=20, null=False, blank=False, choices=diseñoSelect)
    descripcion = models.CharField(max_length=500)
    fechaPost = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} {self.descripcion}"

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, related_name='comentario', on_delete=models.CASCADE, null=False)
    texto = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.user} {self.texto}"
    
class Avatar(models.Model):
    image = models.ImageField(upload_to="avatar")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE)
    receptor = models.CharField(max_length=100)
    texto = models.TextField()

class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=1000)
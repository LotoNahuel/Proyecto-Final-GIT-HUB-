from django import forms
from .models import *
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class ModeloForm(forms.Form):
    class Meta:
        model = Modelo
        fields = ['titulo', 'imagen', 'diseño', 'descripcion', 'emailUsuario']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class RegistroForm(UserCreationForm):
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    email=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["first_name", "last_name", "username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    first_name= forms.CharField(label="Modificar Nombre")
    last_name= forms.CharField(label="Editar Apellido")
    email= forms.EmailField(label="Editar Email")
    password1= forms.CharField(label="Editar Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["first_name", "last_name", "email", "password1", "password2"]
        help_text = {k:"" for k in fields}

class AvatarForm(forms.Form):
    image=forms.ImageField(label="Image")
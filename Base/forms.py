from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class ModeloForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    diseño = forms.CharField(max_length=70)
    descripcion = forms.CharField(max_length=500)
    fechaPost = forms.DateField()
    emailUsuario = forms.EmailField()

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
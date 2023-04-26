from django.shortcuts import render
from .models import *
from .forms import ModeloForm, RegistroForm, UserEditForm
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, "inicio.html")

@login_required
def modelos(request):
    if request.method == "POST":
        form = ModeloForm(request.POST)
        if form.is_valid():
            modelo = Modelo()
            modelo.titulo = form.cleaned_data["titulo"]
            modelo.diseño = form.cleaned_data["diseño"]
            modelo.descripcion = form.cleaned_data["descripcion"]
            modelo.fechaPost = form.cleaned_data["fechaPost"]
            modelo.emailUsuario = form.cleaned_data["emailUsuario"]
            modelo.save()
            form = ModeloForm()
    else:
        form = ModeloForm()

    modelos = Modelo.objects.all()
    return render(request, "carga.html", {"modelos": modelos, "form": form})

@login_required
def otroFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Otro").all()
        return render(request, "otro.html", {"modelos": modelos})
    else:
        return render (request, "otro.html")

@login_required    
def arteFilter(request):
    diseño = ["Arte"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Arte").all()
        return render(request, "arte.html", {"modelos": modelos})
    else:
        return render (request, "arte.html")

@login_required    
def modaFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Moda").all()
        return render(request, "moda.html", {"modelos": modelos})
    else:
        return render (request, "moda.html")

@login_required    
def joyaFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Joyas").all()
        return render(request, "joya.html", {"modelos": modelos})
    else:
        return render(request, "joya.html")

@login_required
def casaFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Casa").all()
        return render(request, "casa.html", {"modelos": modelos})
    else:
        return render(request, "casa.html")

@login_required    
def arquitecturaFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Arquitectura").all()
        return render(request, "arquitectura.html", {"modelos": modelos})
    else:
        return render(request, "arquitectura.html")

@login_required    
def artilugioFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Artilugio").all()
        return render(request, "artilugio.html", {"modelos": modelos})
    else:
        return render(request, "artilugio.html")

@login_required     
def juegoFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Juego").all()
        return render(request, "juego.html", {"modelos": modelos})
    else:
        return render(request, "juego.html")

@login_required 
def herramientaFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Herramienta").all
        return render(request, "herramienta.html", {"modelos": modelos}) 
    else:
        return render(request, "herramienta.html")








#ModificarAndEliminar

@login_required
def eliminarModelo(request, id):
    modelo=Modelo.objects.get(id=id)
    print(modelo)
    modelo.delete()
    modelos=Modelo.objects.all()
    form=ModeloForm()
    return render(request, "carga.html", {"modelos": modelos, "mensaje": "Modelo eliminado", "form": form})

@login_required
def editarModelo(request, id):
    modelo=Modelo.objects.get(id=id)
    if request.method == "POST":
        form = ModeloForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            modelo.titulo=info["titulo"]
            modelo.diseño=info["diseño"]
            modelo.descripcion=info["descripcion"]
            modelo.fechaPost=info["fechaPost"]
            modelo.emailUsuario=info["emailUsuario"]            
            modelo.save()
            modelos = Modelo.objects.all()
            form=ModeloForm()
            return render(request, "carga.html", {"modelos":modelos, "mensaje": "Editado correctamente", "form": form})
        pass
    else:
        formulary= ModeloForm(initial={"titulo":modelo.titulo, "diseño":modelo.diseño, "descripcion":modelo.descripcion, "fechaPost":modelo.fechaPost, "emailUsuario":modelo.emailUsuario})
        return render(request, "modeloform.html", {"form": formulary, "modelo": modelo})

    






#RegisterAndLogin

def register(request):
    if request.method=="POST":
        form= RegistroForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "login.html", {"mensaje": f"Se creo el usuario {username}"})
        else:
            return render(request, "registro.html", {"form": form, "mensaje": "Error al crear el usuario"})
    else:
        form= RegistroForm()
        return render(request, "registro.html", {"form": form})

def login_usuario(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuary=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usuary, password=clave)

            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html", {"mensaje":"A iniciado sesion correctamente"})
            else:
                return render(request, "login.html", {"form": form, "mensaje":"Usuario y/o contraseña incorrectos"})
        else:
            return render(request, "login.html", {"form": form, "mensaje":"Usuario y/o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "login.html", {"form": form})

def editar_usuario(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            return render(request, "inicio.html", {"mensaje": f"Usuario {usuario.username} a sido editado."})
        else:
            return render(request, "editarUsuario.html", {"form": form, "nombreusuario": usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "editarUsuario.html", {"form": form, "nombreusuario":usuario.username})

from django.shortcuts import render
from .models import *
from .forms import ModeloForm, ComentForm, RegistroForm, UserEditForm, AvatarForm
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, "inicio.html", {"avatar": obtenerAvatar(request)})



@login_required
def modelos(request):
    if request.method == "POST":
        form = ModeloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ModeloForm()
    else:
        form = ModeloForm()

    modelos = Modelo.objects.all()
    return render(request, "carga.html", {"modelos": modelos, "form": form, "avatar": obtenerAvatar(request)})

@login_required
def otroFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Otro").all()
        return render(request, "otro.html", {"modelos": modelos, "avatar": obtenerAvatar(request)})
    else:
        return render (request, "otro.html")

@login_required    
def arteFilter(request):
    diseño = ["Arte"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Arte").all()
        return render(request, "arte.html", {"modelos": modelos, "avatar": obtenerAvatar(request)})
    else:
        return render (request, "arte.html")

@login_required    
def modaFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Moda").all()
        return render(request, "moda.html", {"modelos": modelos, "avatar": obtenerAvatar(request)})
    else:
        return render (request, "moda.html")

@login_required    
def joyaFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Joyas").all()
        return render(request, "joya.html", {"modelos": modelos, "avatar": obtenerAvatar(request)})
    else:
        return render(request, "joya.html")

@login_required
def casaFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Casa").all()
        return render(request, "casa.html", {"modelos": modelos, "avatar": obtenerAvatar(request)})
    else:
        return render(request, "casa.html")

@login_required    
def arquitecturaFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Arquitectura").all()
        return render(request, "arquitectura.html", {"modelos": modelos, "avatar": obtenerAvatar(request)})
    else:
        return render(request, "arquitectura.html")

@login_required    
def artilugioFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Artilugio").all()
        return render(request, "artilugio.html", {"modelos": modelos, "avatar": obtenerAvatar(request)})
    else:
        return render(request, "artilugio.html")

@login_required     
def juegoFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Juego").all()
        return render(request, "juego.html", {"modelos": modelos, "avatar": obtenerAvatar(request)})
    else:
        return render(request, "juego.html")

@login_required 
def herramientaFilter(request):
    diseño = ["diseño"]
    if diseño != "":
        modelos = Modelo.objects.filter(diseño__icontains="Herramienta").all
        return render(request, "herramienta.html", {"modelos": modelos, "avatar": obtenerAvatar(request)}) 
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
            modelo.imagen=info["imagen"]
            modelo.diseño=info["diseño"]
            modelo.descripcion=info["descripcion"]
            modelo.fechaPost=info["fechaPost"]         
            modelo.save()
            modelos = Modelo.objects.all()
            form=ModeloForm()
            return render(request, "carga.html", {"modelos":modelos, "mensaje": "Editado correctamente", "form": form})
        else:
            formulary= ModeloForm(initial={"titulo":modelo.titulo, "diseño":modelo.diseño, "descripcion":modelo.descripcion, "fechaPost":modelo.fechaPost})
            return render(request, "modeloform.html", {"form": formulary, "modelo": modelo, "avatar": obtenerAvatar(request), "mensaje": "Error al subir los datos"})
    else:
        formulary= ModeloForm(initial={"titulo":modelo.titulo, "diseño":modelo.diseño, "descripcion":modelo.descripcion, "fechaPost":modelo.fechaPost})
        return render(request, "modeloform.html", {"form": formulary, "modelo": modelo, "avatar": obtenerAvatar(request)})
    
@login_required
def comentarios(request):
    if request.method == "POST":
        form = ComentForm(request.POST)
        if form.is_valid():
            comentario = Comentario()
            comentario.texto = form.cleaned_data["texto"]
            comentario.nombre = form.cleaned_data["nombre"]
            comentario.save()
            form = ComentForm()
    else:
        form = ComentForm()
        
    comentarios = Comentario.objects.all()
    return render(request, "otro.html", {"form": form, "comentarios": comentarios, "avatar": obtenerAvatar(request)})
    

    






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
        return render(request, "login.html", {"form": form, "usuario": usuario})
    
def perfil(request):
    usuario=request.user
    if request.method=="GET":
        return render(request, "perfil.html", {"mensaje":usuario.username, "avatar": obtenerAvatar(request)})

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
            return render(request, "editarUsuario.html", {"form": form, "nombreusuario": usuario.username, "avatar": obtenerAvatar(request)})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "editarUsuario.html", {"form": form, "nombreusuario":usuario.username, "avatar": obtenerAvatar(request)})


def obtenerAvatar(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].image.url
    else:
        return "/media/avatar/default.png"
    

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, image=request.FILES["image"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len (avatarViejo)>0:
                (avatarViejo)[0].delete()
            avatar.save()
            return render(request, "inicio.html", {"mensaje": "Avatar agregado", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje": "Error al guardar el archivo", "avatar": obtenerAvatar(request)})
    else:
        form=AvatarForm()
        return render(request, "agregarAvatar.html", {"form": form, "usuario": request.user, "avatar": obtenerAvatar(request)})
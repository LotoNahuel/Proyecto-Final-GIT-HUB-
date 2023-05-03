from django.shortcuts import render
from .models import *
from .forms import ModeloForm, ComentForm, RegistroForm, UserEditForm, AvatarForm, MensajeForm, PerfilForm
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

    
def perfil(request):
    usu=request.user.id
    usuario = ["usuario"]
    if usuario == usu:
        perfil = Perfil.objects.all()
        return render(request, "perfil.html", {"perfil": perfil, "usu":request.user, "avatar": obtenerAvatar(request)})
    else:
        return render (request, "perfil.html")

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
        modelos = Modelo.objects.filter(diseño__icontains="Herramienta").all()
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
        form = ModeloForm(request.POST, request.FILES)
        if form.is_valid():
            modeloViejo=modelo            
            modeloViejo.delete()
            form.save()
            modelos = Modelo.objects.all()
            form=ModeloForm()
            return render(request, "carga.html", {"modelos":modelos, "mensaje": "Editado correctamente", "form": form})
        pass
    else:
        formulary= ModeloForm(initial={"titulo":modelo.titulo, "diseño":modelo.diseño, "descripcion":modelo.descripcion, "fechaPost":modelo.fechaPost})
        return render(request, "modeloform.html", {"form": formulary, "modelo": modelo, "avatar": obtenerAvatar(request)})
    


#Comentarios

@login_required
def comentarios(request):
    if request.method == "POST":
        form = ComentForm(request.POST)
        if form.is_valid():
            form.save()
            form = ComentForm()
    else:
        form = ComentForm()
        
    comentarios = Comentario.objects.all()
    return render(request, "comentarios.html", {"form": form, "comentarios": comentarios, "avatar": obtenerAvatar(request)})

@login_required
def comentFilter(request):
    modelo = ["modelo"]
    user=request.user.id
    if modelo != "":
        comentario = Comentario.objects.filter(modelo=user).all()
        return render(request, "carga.html", {"comentario": comentario, "avatar": obtenerAvatar(request)})
    else:
        return render(request, "carga.html", {"sino": "No hay comentarios"})
    

#Mensajes

def mensajes(request):
    if request.method == "Post":
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            form = MensajeForm()
    else:
        form = MensajeForm()
    mensajes = Mensaje.objects.all()
    return render(request, {"form": form, "mensajes": mensajes, "avatar": obtenerAvatar(request)})

def receptor(request):
    receptor = ["receptor"]
    user = request.user
    if user in receptor:
        mensaje = Mensaje.objects.all()
        return render(request, {"mensaje": mensaje, "avatar": obtenerAvatar(request)})
    else:
        return render(request, {"recibido": "no hay mensajes recibidos"})
    
def emisor(request):
    emisor = ["emisor"]
    user = request.user.id
    if user in emisor:
        mensajes = Mensaje.objects.all()
        return render(request, {"mensajes": mensajes, "avatar": obtenerAvatar(request)})
    else:
        return render(request, {"enviado": "no hay mensajes enviados"})



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
                return render(request, "inicio.html", {"mensaje":"A iniciado sesion correctamente", "avatar": obtenerAvatar(request)})
            else:
                return render(request, "login.html", {"form": form, "mensaje":"Usuario y/o contraseña incorrectos"})
        else:
            return render(request, "login.html", {"form": form, "mensaje":"Usuario y/o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "login.html", {"form": form})

@login_required   
def perfilEdit(request):
    if request.method=="POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            perfil=Perfil(usuario=request.user, text=request.POST["text"])
            perfilViejo=Perfil.objects.filter(usuario=request.user)
            if len (perfilViejo)>0:
                (perfilViejo)[0].delete()
            perfil.save()
            return render(request, "perfil.html", {"avatar": obtenerAvatar(request)})
        pass
    else:
        form=PerfilForm()
    return render(request, "perfilEdit.html", {"form": form, "avatar": obtenerAvatar(request)})

@login_required    
def perfil(request):
    usuario = ["usuario"]
    user=request.user.id
    if usuario != "":
        perfil = Perfil.objects.filter(usuario=user).all()
        return render(request, "perfil.html", {"perfil": perfil, "usu":request.user, "avatar": obtenerAvatar(request)})
    else:
        return render (request, "perfil.html", {"usu":request.user, "mensaje": "No hay descripcion", "avatar": obtenerAvatar(request)})

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
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="inicio"),
    path("modelos/", modelos, name="modelos"),
    path('comentarios/', comentarios, name="comentarios"),
    path("otroFilter/", otroFilter, name="otroFilter"),
    path("arteFilter/", arteFilter, name="arteFilter"),
    path("modaFilter/", modaFilter, name="modaFilter"),
    path("joyaFilter/", joyaFilter, name="joyaFilter"),
    path("casaFilter/", casaFilter, name="casaFilter"),
    path("arquitecturaFilter/", arquitecturaFilter, name="arquitecturaFilter"),
    path("artilugioFilter/", artilugioFilter, name="artilugioFilter"),
    path("juegoFilter/", juegoFilter, name="juegoFilter"),
    path("herramientaFilter/", herramientaFilter, name="herramientaFilter"),

    path("eliminarModelo/<id>", eliminarModelo, name="eliminarModelo"),
    path("editarModelo/<id>", editarModelo, name="editarModelo"),

    path("login/", login_usuario, name="login"),
    path("register/", register, name="registro"),
    path("logout/", LogoutView.as_view(), name="logout"), #Por si quiero cambiar template_name="logout.html"
    path("editarUsuario/", editar_usuario, name="editarUsuario"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    path("perfil/", perfil, name="perfil"),
    path("perfilEdit/", perfilEdit, name="perfilEdit"),

    path("mensajes/", mensajes, name="mensajes"),
    path("emisorAndReceptor/", emisorAndReceptor, name="emisorAndReceptor"),
    path("about/", about, name="about"),
]
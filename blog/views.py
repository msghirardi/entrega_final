from asyncio import DatagramTransport
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Jurisprudencia, Letrado, Seccion
from django.urls import reverse

from blog.forms import JurisprudenciaForm, SeccionForm, LetradoForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.models import Avatar, Letrado
from blog.forms import AvatarForm, UserEditionForm


# Create your views here.


@login_required
def buscar(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda.html")

    if request.method == "POST":
        titulo_para_buscar = request.POST["titulo"]
        resultados_de_busqueda = Jurisprudencia.objects.filter(
            titulo=titulo_para_buscar
        )
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultado-de-busqueda.html", contexto)


@login_required
def mostrar_inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}

    return render(request, "blog/inicio.html", contexto)


def acerca_de_mi(request):
    return render(request, "blog/about.html")


def volver_atras(request):
    return render(request, "blog/volver.html")


@login_required
def procesar_formulario_jurisprudencia(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method == "GET":
        mi_formulario = JurisprudenciaForm()
        contexto = {"formulario": mi_formulario, "avatar": avatar.imagen.url}
        return render(request, "blog/formulario-jurisprudencia.html", contexto)

    if request.method == "POST":

        mi_formulario = JurisprudenciaForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Jurisprudencia(
                titulo=datos_ingresados_por_usuario["titulo"],
                texto=datos_ingresados_por_usuario["texto"],
                fecha=datos_ingresados_por_usuario["fecha"],
            )
            nuevo_modelo.save()

            return render(request, "blog/exito.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-jurisprudencia.html", contexto)


@login_required
def procesar_formulario_letrado(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method == "GET":
        mi_formulario = LetradoForm()
        contexto = {"formulario": mi_formulario, "avatar": avatar.imagen.url}
        return render(request, "blog/formulario-letrados.html", contexto)

    if request.method == "POST":

        mi_formulario = LetradoForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Letrado(
                nombre=datos_ingresados_por_usuario["nombre"],
                apellido=datos_ingresados_por_usuario["apellido"],
                fuero=datos_ingresados_por_usuario["fuero"],
            )
            nuevo_modelo.save()

            return render(request, "blog/exito.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-letrados.html", contexto)


@login_required
def procesar_formulario_seccion(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    mi_formulario = SeccionForm()
    contexto = {"formulario": mi_formulario, "avatar": avatar.imagen.url}
    return render(request, "blog/formulario-seccion.html", contexto)


def leer_letrado(request):
    letrados = Letrado.objects.all()
    avatar = Avatar.objects.filter(user=request.user).first()
    contexto = {"letrados": letrados, "avatar": avatar.imagen.url}
    return render(request, "blog/leer-letrado.html", contexto)


@login_required
def eliminar_letrado(request, letrado_nombre):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    letrado = Letrado.objetcs.get(nombre=letrado_nombre)
    letrado.delete()
    # Vuelvo al menu
    letrados = Letrado.objects.all()
    contexto = {"letrados": letrados, "avatar": avatar.imagen.url}
    return render(request, "blog/leer-letrado.html", contexto)


@login_required
def listar_jurisprudencia(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    todos_los_jurisprudencia = Jurisprudencia.objects.all()
    contexto = {
        "jurisprudencia_encontrados": todos_los_jurisprudencia,
        "avatar": avatar.imagen.url,
    }
    return render(request, "blog/listar-jurisprudencia.html", contexto)


# EL LOGIN REQUIRED MIXIN
class JurisprudenciaList(ListView, LoginRequiredMixin):
    model = Jurisprudencia
    template_name = "blog/jurisprudencia-list.html"


class JurisprudenciaCreacion(LoginRequiredMixin, CreateView):
    model = Jurisprudencia
    fields = ["titulo", "texto"]

    def get_success_url(self):
        return reverse("JurisprudenciaList")


class JurisprudenciaUpdateView(LoginRequiredMixin, UpdateView):
    model = Jurisprudencia
    success_url = "/blog/jurisprudencia/list"
    fields = ["titulo", "fecha"]


class JurisprudenciaDelete(LoginRequiredMixin, DeleteView):
    model = Jurisprudencia
    success_url = "/blog/jurisprudencia/list"


class JurisprudenciaDetalle(LoginRequiredMixin, DetailView):
    model = Jurisprudencia
    template_name = "blog/jurisprudencia-detalle.html"


class MyLogin(LoginView):
    template_name = "blog/login.html"


class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "blog/logout.html"


def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


# Eto es lo que muestra la slide de CODER
# Yo prefiero usar MyLogin
def login_request(request):

    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "blog/login.html", {"form": form})

    form = AuthenticationForm(request, data=request.POST)

    if not form.is_valid():
        return render(
            request,
            "blog/inicio.html",
            {"mensaje": "Error: los datos ingresados no son correctos"},
        )
    else:
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            return render(
                request, "blog/inicio.html", {"mensaje": f"Bienvenido {username}"}
            )
        else:
            return render(
                request,
                "blog/inicio.html",
                {"mensaje": "El usuario no existe en nuestra appliación"},
            )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "blog/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "blog/registro.html", {"form": form})


# VER ESTO!!!!!


@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "blog/inicio.html", {"avatar": avatar.imagen.url})

    contexto = {"user": user, "form": form, "avatar": avatar.imagen.url}
    return render(request, "blog/editarPerfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "blog/inicio.html")

    contexto = {"form": form}
    return render(request, "blog/avatar_form.html", contexto)

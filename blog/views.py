from asyncio import DatagramTransport
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Jurisprudencia, Letrado, Seccion

from blog.forms import JurisprudenciaForm, SeccionForm, LetradoForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.


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


def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


def procesar_formulario_jurisprudencia(request):
    if request.method == "GET":
        mi_formulario = JurisprudenciaForm()
        contexto = {"formulario": mi_formulario}
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


def procesar_formulario_letrado(request):
    if request.method == "GET":
        mi_formulario = LetradoForm()
        contexto = {"formulario": mi_formulario}
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


def procesar_formulario_seccion(request):
    mi_formulario = SeccionForm()
    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-seccion.html", contexto)


def leer_letrado(request):
    letrados = Letrado.objects.all()
    contexto = {"letrados": letrados}
    return render(request, "blog/leer-letrado.html", contexto)


def eliminar_letrado(request, letrado_nombre):
    letrado = Letrado.objetcs.get(nombre=letrado_nombre)
    letrado.delete()
    # Vuelvo al menu
    letrados = Letrado.objects.all()
    contexto = {"letrados": letrados}
    return render(request, "blog/leer-letrado.html", contexto)


def listar_jurisprudencia(request):
    todos_los_jurisprudencia = Jurisprudencia.objects.all()
    contexto = {"jurisprudencia_encontrados": todos_los_jurisprudencia}
    return render(request, "blog/listar-jurisprudencia.html", contexto)


class JurisprudenciaList(ListView):
    model = Jurisprudencia
    template_name = "blog/jurisprudencia-list.html"


from django.urls import reverse


class JurisprudenciaCreacion(CreateView):
    model = Jurisprudencia
    fields = ["nombre", "camada"]

    def get_success_url(self):
        return reverse("JurisprudenciaList")


class JurisprudenciaUpdateView(UpdateView):
    model = Jurisprudencia
    success_url = "/blog/jurisprudencia/list"
    fields = ["nombre", "camada"]


class JurisprudenciaDelete(DeleteView):
    model = Jurisprudencia
    success_url = "/blog/jurisprudencia/list"


class JurisprudenciaDetalle(DetailView):
    model = Jurisprudencia
    template_name = "blog/jurisprudencia-detalle.html"

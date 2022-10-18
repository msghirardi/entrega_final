from __future__ import barry_as_FLUFL
from asyncio import DatagramTransport
from multiprocessing import context
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Jurisprudencia

from blog.forms import JurisprudenciaForm, SeccionForm, LetradoForm

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
        return render(request, "blog/resultado-de-busqueda.html", context=contexto)


def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


def procesar_formulario_jurisprudencia(request):
    if request.method == "GET":
        mi_formulario = JurisprudenciaForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-jurisprudencia.html", context=contexto)

    if request.method == "POST":

        mi_formulario = JurisprudenciaForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Jurisprudencia(
                titulo=datos_ingresados_por_usuario["titulo"],
                texto=datos_ingresados_por_usuario["texto"],
                # fecha=datos_ingresados_por_usuario["fecha"],
            )
            nuevo_modelo.save()

            return render(request, "blog/exito.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-jurisprudencia.html", context=contexto)


def procesar_formulario_letrado(request):
    mi_formulario = LetradoForm()
    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-letrados.html", context=contexto)


def procesar_formulario_seccion(request):
    mi_formulario = SeccionForm()
    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-seccion.html", context=contexto)

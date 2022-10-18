from django.urls import path, include
from blog.views import (
    procesar_formulario_jurisprudencia,
    procesar_formulario_letrado,
    procesar_formulario_seccion,
    buscar,
    mostrar_inicio,
    leer_letrado,
)

urlpatterns = [
    path(
        "formulario-jurisprudencia/",
        procesar_formulario_jurisprudencia,
    ),
    path("formulario-seccion/", procesar_formulario_seccion),
    path("formulario-letrado/", procesar_formulario_letrado),
    path("buscar-articulo/", buscar),
    path("inicio/", mostrar_inicio),
    path("leer-letrado/", leer_letrado),
]

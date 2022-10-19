from django.urls import path
from blog.views import (
    procesar_formulario_jurisprudencia,
    procesar_formulario_letrado,
    procesar_formulario_seccion,
    buscar,
    mostrar_inicio,
    leer_letrado,
    listar_jurisprudencia,
    JurisprudenciaDelete,
    JurisprudenciaDetalle,
    JurisprudenciaUpdateView,
    JurisprudenciaList,
    JurisprudenciaCreacion,
)

urlpatterns = [
    path(
        "formulario-jurisprudencia/",
        procesar_formulario_jurisprudencia,
    ),
    path("formulario-seccion/", procesar_formulario_seccion),
    path("formulario-letrado/", procesar_formulario_letrado),
    path("buscar-jurisprudencia/", buscar),
    path("inicio/", mostrar_inicio),
    path("leer-letrado/", leer_letrado),
    path("jurisprudencia-lista/", listar_jurisprudencia),
    path(
        "jurisprudencia/list", JurisprudenciaList.as_view(), name="JurisprudenciaList"
    ),
    path(
        "r'(?P<pk>\d+)^$'", JurisprudenciaDetalle.as_view(), name="JurisprudenciaDetail"
    ),
    path(
        "jurisprudencia-nuevo/",
        JurisprudenciaCreacion.as_view(),
        name="JurisprudenciaNew",
    ),
    path(
        "editar/<pk>", JurisprudenciaUpdateView.as_view(), name="JurisprudenciaUpdate"
    ),
    path("borrar/<pk>", JurisprudenciaDelete.as_view(), name="JurisprudenciaDelete"),
]

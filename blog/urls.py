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
        name="Ingresar Jurisprudencia",
    ),
    path("formulario-seccion/", procesar_formulario_seccion, name="Ingrese Seccion"),
    path("formulario-letrado/", procesar_formulario_letrado, name="Ingrese Letrado"),
    path("buscar-jurisprudencia/", buscar, name="Buscar Jurisprudencia"),
    path("inicio/", mostrar_inicio, name="Inicio"),
    path("leer-letrado/", leer_letrado, name="Ver Letrados"),
    path("jurisprudencia-lista/", listar_jurisprudencia, name="Listar Jurisprudencia"),
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

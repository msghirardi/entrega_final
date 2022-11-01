from django.urls import path
from blog.views import (
    procesar_formulario_jurisprudencia,
    procesar_formulario_letrado,
    procesar_formulario_seccion,
    buscar,
    mostrar_inicio,
    leer_letrado,
    listar_jurisprudencia,
    acerca_de_mi,
    JurisprudenciaDelete,
    JurisprudenciaDetalle,
    JurisprudenciaUpdateView,
    JurisprudenciaList,
    JurisprudenciaCreacion,
    MyLogin,
    MyLogout,
    mostrar_inicio,
    register,
    editar_perfil,
    agregar_avatar,
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
    path("pages/", listar_jurisprudencia, name="Listar Jurisprudencia"),
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
    path("about/", acerca_de_mi, name="About"),
    path("inicio/", mostrar_inicio, name="Inicio"),
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    path("register/", register, name="Register"),
    path(
        "jurisprudencia/<pk>'",
        JurisprudenciaDetalle.as_view(),
        name="jurisprudenciaDetail",
    ),
    path("editar-perfil/", editar_perfil, name="EditarPerfil"),
    path("agregar-avatar/", agregar_avatar, name="AgregarAvatar"),
    path("", mostrar_inicio),
]

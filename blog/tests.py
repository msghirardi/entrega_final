from django.test import TestCase

from datetime import datetime

from blog.models import Letrado


class ViewTestCase(TestCase):
    def test_crear_letrado(self):
        Letrado.objects.create(nombre="letrado 1234", apellido="gomez")
        todos_los_letrados = Letrado.objects.all()
        assert len(todos_los_letrados) == 1
        assert todos_los_letrados[0].nombre == "letrado 1234"

    def test_crear_letrado_sin_fuero(self):
        Letrado.objects.create(nombre="letrado 1234", apellido="gomez")
        todos_los_letrados = Letrado.objects.all()
        assert todos_los_letrados[0].apellido == "gomez"

    def test_crear_4_letrados(self):
        Letrado.objects.create(nombre="letrado 01", apellido=1)
        Letrado.objects.create(nombre="letrado 02", apellido=2)
        Letrado.objects.create(nombre="letrado 03", apellido=3)
        Letrado.objects.create(nombre="letrado 04", apellido=4)
        Letrado.objects.create(nombre="letrado 05", apellido=5)
        todos_los_letrados = Letrado.objects.all()
        assert len(todos_los_letrados) == 5

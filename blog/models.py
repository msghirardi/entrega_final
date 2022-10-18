from unittest.util import _MAX_LENGTH
from urllib import request
from django.db import models

# Create your models here.


class Letrado(models.Model):
    class Meta:
        verbose_name_plural = "Letrados"

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fuero = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Jurisprudencia(models.Model):
    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=1000)
    fecha = models.DateField(null=True)


def __str__(self):
    return self.titulo


class Seccion(models.Model):
    class Meta:
        verbose_name_plural = "Secciones"

    nombre = models.CharField(max_length=30)

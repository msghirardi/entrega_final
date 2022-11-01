from unittest.util import _MAX_LENGTH
from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Letrado(models.Model):
    class Meta:
        verbose_name_plural = "Letrados"

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fuero = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Fuero {self.fuero}"


class Jurisprudencia(models.Model):
    class Meta:
        verbose_name_plural = "Jurisprudencia"

    titulo = models.CharField(max_length=70)
    texto = models.CharField(max_length=100000)
    fecha = models.DateField(null=True)

    def __str__(self):
        return f"Titulo: {self.titulo} - Texto: {self.texto} - Fecha: {self.fecha}"


def __str__(self):
    return {self.titulo}


class Seccion(models.Model):
    class Meta:
        verbose_name_plural = "Secciones"

    nombre = models.CharField(max_length=30)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

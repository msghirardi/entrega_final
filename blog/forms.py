from django import forms


class JurisprudenciaForm(forms.Form):
    titulo = forms.CharField(max_length=30)
    texto = forms.CharField(max_length=1000)
    fecha = forms.DateField()


class LetradoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    profesion = forms.CharField(max_length=30)


class SeccionForm(forms.Form):
    titulo = forms.CharField(max_length=30)

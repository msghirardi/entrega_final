from django.contrib import admin
from blog.models import Letrado, Seccion, Jurisprudencia

# Register your models here.
admin.site.register(Jurisprudencia)
admin.site.register(Seccion)
admin.site.register(Letrado)

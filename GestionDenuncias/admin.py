from django.contrib import admin

# Register your models here.
from .models import Denuncias,Abogados

admin.site.register(Denuncias)
admin.site.register(Abogados)
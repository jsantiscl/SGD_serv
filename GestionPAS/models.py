from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class DenunciaPas(models.Model):
    folio = models.CharField(max_length=200)
    fecha_ingreso_registro = models.DateField(auto_now_add=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    presunto_infractor = models.CharField(max_length=200)
    eleccion = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    actuacion = models.CharField(max_length=200)
    reporte = models.CharField(max_length=200)
    expediente = models.CharField(max_length=200)
    asignacion_fiscal = models.CharField(max_length=200)
    vencimiento = models.DateField(null=True, blank=True)
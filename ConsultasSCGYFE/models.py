from django.db import models

class ConsultasFormulario(models.Model):

    ObjectID = models.IntegerField(primary_key=True)
    GlobalID = models.CharField(max_length=500, default='SIN')
    NombreCompleto = models.CharField(max_length=200, null=True, blank=True)
    Rut = models.CharField(max_length=50, null=True, blank=True)
    TemaAsociado = models.CharField(max_length=50, null=True, blank=True)
    Pregunta = models.CharField(max_length=1000, null=True, blank=True)
    Email = models.CharField(max_length=50, default='SIN')
    FechaIngreso = models.DateTimeField(null=True, blank=True)
    Respondido = models.BooleanField(default=False)
    RespondidoPor = models.CharField(max_length=50, null=True, blank=True)
    Fecha_Respuesta = models.DateTimeField(null=True, blank=True)
    Respuesta = models.CharField(max_length=2000, null=True, blank=True)
    Etapa = models.CharField(max_length=50, default='1_Nueva')
    def __str__(self):
        return self.ObjectID

class WorkflowConsultas(models.Model):
    AutoID = models.AutoField(primary_key=True)
    ObjectID = models.IntegerField()
    GlobalID = models.CharField(max_length=500, default='SIN')
    Usuario = models.CharField(max_length=500, default='SIN')
    NuevaEtapa = models.CharField(max_length=500, default='SIN')
    FechaCambio = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.ObjectID
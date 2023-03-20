from django.db import models

class Candidatos(models.Model):
    eleccion = models.CharField(max_length=100)
    region = models.CharField(max_length=200, null=True, blank=True)
    territorio_electoral = models.CharField(max_length=200, null=True, blank=True)
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=200)
    apellido_p = models.CharField(max_length=200)
    apellido_m = models.CharField(max_length=200)
    sexo = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    pacto = models.CharField(max_length=100, null=True, blank=True)
    subpacto = models.CharField(max_length=100, null=True, blank=True)
    partido = models.CharField(max_length=100, null=True, blank=True)
    rut_admin = models.ForeignKey('AdministradoresElectorales', on_delete=models.SET_NULL, null=True, blank=True, related_name='candidatos')
    partido_asociado = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=100, default='1_Ingreso')
    link_edicion = models.URLField(max_length=500, default='https://serv.jasb.cl')
    link_visualizacion = models.URLField(max_length=500, default='https://serv.jasb.cl')
    class Meta:
        unique_together = ('eleccion', 'rut')
    def __str__(self):
        return f"{self.eleccion} - {self.rut}"

class AdministradoresElectorales(models.Model):
    rut_admin = models.CharField(max_length=20, primary_key=True)
    nombre_admin  = models.CharField(max_length=200)
    apellido_p_admin  = models.CharField(max_length=200)
    apellido_m_admin  = models.CharField(max_length=200)
    email_admin  = models.CharField(max_length=200)
    telefono_admin = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.rut_admin

class Partidos(models.Model):
    eleccion = models.CharField(max_length=100)
    par_rut = models.CharField(max_length=20)
    par_nombre = models.CharField(max_length=200)
    par_rut_admin = models.ForeignKey('AdministradoresGenerales', on_delete=models.SET_NULL, null=True, blank=True, related_name='partidos')
    par_mail = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=100, default='1_Ingreso')
    link_edicion = models.URLField(max_length=500, default='https://serv.jasb.cl')
    link_visualizacion = models.URLField(max_length=500, default='https://serv.jasb.cl')
    class Meta:
        unique_together = ('eleccion', 'par_rut')

    def __str__(self):
        return f"{self.eleccion} - {self.par_rut} - {self.par_nombre}"


class AdministradoresGenerales(models.Model):
    par_rut_admin = models.CharField(max_length=20, primary_key=True)
    nombre_age  = models.CharField(max_length=200)
    apellido_p_age  = models.CharField(max_length=200)
    apellido_m_age  = models.CharField(max_length=200)
    correo_age  = models.CharField(max_length=200)
    telefono  = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.par_rut_admin
class WorkflowSCP(models.Model):
    AutoID = models.AutoField(primary_key=True)
    rut_candidato_partido = models.CharField(max_length=500, default='SIN')
    usuario = models.CharField(max_length=500, default='SIN')
    nueva_etapa = models.CharField(max_length=500, default='SIN')
    fecha_cambio = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"{self.rut_candidato_partido} - {self.usuario} - {self.nueva_etapa}"

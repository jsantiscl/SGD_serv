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
    asignado_a= models.CharField(max_length=100, default='Pendiente')
    observacion_rechazo = models.CharField(max_length=5000, null=True, blank=True)
    respuesta = models.CharField(max_length=100, default='NO')
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
    asignado_a = models.CharField(max_length=100, default='Pendiente')
    observacion_rechazo = models.CharField(max_length=5000, null=True, blank=True)
    respuesta = models.CharField(max_length=100, default='NO')
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

class AportesSRA(models.Model):
    folio = models.IntegerField()
    fecha_aporte = models.DateTimeField()
    tipo_aporte = models.CharField(max_length=100)
    rut_aportante = models.CharField(max_length=20,null=True, blank=True)
    nombre_aportante = models.CharField(max_length=200,null=True, blank=True)
    tipo_aportante = models.CharField(max_length=100)
    monto = models.BigIntegerField()
    rut_candidato_o_partido = models.CharField(max_length=20)
    nombre_candidato_o_partido = models.CharField(max_length=200)
    tipo_donatario = models.CharField(max_length=100)
    estado_aporte = models.CharField(max_length=100)
    fecha_aprobacion = models.DateTimeField(null=True, blank=True)
    fecha_abono = models.DateTimeField(null=True, blank=True)
    tipo_pago = models.CharField(max_length=100)
    estado_servel = models.CharField(max_length=100)
    fecha_hora_actualizado = models.DateTimeField()
    semana = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.folio} - {self.rut_aportante} - {self.nombre_aportante}"

class rel_candidato(models.Model):
    AutoID = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=30, default='SIN')
    cod = models.CharField(max_length=10, default='SIN')
    def __str__(self):
        return f"{self.rut_candidato_partido} - {self.usuario} - {self.nueva_etapa}"


class rel_partido(models.Model):
    AutoID = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=30, default='SIN')
    cod = models.CharField(max_length=10, default='SIN')

    def __str__(self):
        return f"{self.rut_candidato_partido} - {self.usuario} - {self.nueva_etapa}"

class Cartolas(models.Model):
    rut = models.CharField(max_length=12)
    tipo = models.CharField(max_length=10)
    cuenta = models.CharField(max_length=15)
    fec_emi = models.DateField()
    n_cart = models.IntegerField()
    corr = models.IntegerField()
    num_doc = models.CharField(max_length=50,null=True, blank=True)
    descripcion = models.CharField(max_length=50)
    ofi = models.IntegerField()
    sal_cargos = models.BigIntegerField(null=True, blank=True)
    sal_abonos = models.BigIntegerField(null=True, blank=True)
    f_mov = models.DateField()
    saldo = models.BigIntegerField(null=True, blank=True)
    m = models.CharField(max_length=2)
    tc = models.IntegerField()

    def __str__(self):
        return f"{self.rut} - {self.cuenta} - {self.descripcion}"


class RespuestasCP(models.Model):

    ObjectID = models.IntegerField(primary_key=True)
    GlobalID = models.CharField(max_length=500, default='SIN')
    NombreCompleto = models.CharField(max_length=200, null=True, blank=True)
    Rut = models.CharField(max_length=50, null=True, blank=True)
    TemaAsociado = models.CharField(max_length=50, null=True, blank=True)
    Pregunta = models.CharField(max_length=1000, null=True, blank=True)
    Email = models.CharField(max_length=50, default='SIN')
    FechaIngreso = models.DateTimeField(null=True, blank=True)
    AsignadoA = models.BooleanField(max_length=50, null=True, blank=True)
    TipoAsignacion = models.CharField(max_length=50, null=True, blank=True)
    Etapa = models.CharField(max_length=50, default='1_Nueva')
    Adjunto= models.CharField(max_length=1000, null=True, blank=True)
    Candidato_o_Partido = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.ObjectID

class Tokens(models.Model):

    Token = models.CharField(max_length=1000, default='SIN')
    Fecha = models.DateTimeField(null=True, blank=True)

class F87_F88(models.Model):
    tpo = models.CharField(max_length=50, null=True, blank=True)
    rut = models.CharField(max_length=200, null=True, blank=True)
    rut_cp = models.CharField(max_length=200, null=True, blank=True)
    dv_cp = models.CharField(max_length=200, null=True, blank=True)
    fecha_d = models.DateField(null=True, blank=True)
    tpo_i = models.CharField(max_length=200, null=True, blank=True)
    rut_ap = models.CharField(max_length=200, null=True, blank=True)
    dv_ap = models.CharField(max_length=200, null=True, blank=True)
    nom_ap = models.CharField(max_length=200, null=True, blank=True)
    num_doc = models.CharField(max_length=200, null=True, blank=True)
    cod_tc = models.CharField(max_length=200, null=True, blank=True)
    cod_td = models.CharField(max_length=200, null=True, blank=True)
    glosa = models.CharField(max_length=500, null=True, blank=True)
    monto = models.BigIntegerField( null=True, blank=True)
    tpo_r = models.CharField(max_length=20, null=True, blank=True)
    hoja = models.CharField(max_length=20, null=True, blank=True)
    linea = models.CharField(max_length=20, null=True, blank=True)


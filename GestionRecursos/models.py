from django.db import models

# Create your models here.
class UsersRecursos(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)
    habilitado = models.BooleanField(default=True)
    username = models.CharField(max_length=50, default='SIN')
    iniciales = models.CharField(max_length=50, default='NODEFINIDA')
    celula = models.CharField(max_length=50, default='NoDefinida')
    tipo = models.CharField(max_length=50, default='Auditor_jr')
    def __str__(self):
        return self.nombre

class UsersPlebiscito(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)
    habilitado = models.BooleanField(default=True)
    username = models.CharField(max_length=50, default='SIN')
    iniciales = models.CharField(max_length=50, default='NODEFINIDA')
    celula = models.CharField(max_length=50, default='NoDefinida')
    tipo = models.CharField(max_length=50, default='Auditor_jr')
    def __str__(self):
        return self.nombre

class Recursos(models.Model):
    Estados = (
        ("LD_asignacion_Lider", "1 -(Rep) En Asignacion Lider"),
        ("JC_asignacion_jefe_celula", "2 -(Rep) En Asignacion Jefe Celula"),
        ("AU_realizacion_informe_tecnico", "3 -(Rep) Informe Tecnico"),
        ("JC_analisis_caso_jefe_celula", "4 -(Rep) Analisis de Informe Generado"),
        ("ADMIN_devuelto_para_reclasificacion", " 0 - Devuelto para Reclasificacion"),
        ("AB_elaboracion_Propuesta", "5 -(Rep) En Elaboracion Propuesta Resolucion"),
        ("JC_Validacion ", "6 -(Rep) En Validacion Jefe Celula"),  # cambiar fase anterior
        ("ABVAL_revision_propuesta", "7 -(Rep) En Validacion Propuesta Resolucion"),
        ("AB_elaboracion_Propuesta_devuelto", "7.5 -(Rep) Devuelto para Revisión Abogado"),
        ("LD_en_validacion_lider ", "8 -(Rep) En Validacion Lider"),
        ("JD_en_validacion_jd ", "9 -(Rep) En Validacion Jefe Division"),
        ("SD_en_validacion_sd ", "10 -(Rep) En Validacion Subdirector"),
        ("GD_Subir_sistema_datasoft", "11 -(Rep) Subir a Sistema Datasoft"),  #Lo Debe pasar a PDF
        ("GD_en_firma_director", "12 -(Rep) En Firma Director"),
        ("GD_en_Notificacion", "13 -(Rep) En Notificacion"),
        ("GD_subida_sge", "14 -(Rep) Subir a SGE"),
        ("fin_proceso_finalizado", "99 - Proceso Finalizado"),  #Aca llegan por flujo si son Reposicion // Evento Terminal de todos
        ("LD_AC_Analisis_rep_subsidio", "15 - Analisis Reposicion con Subsidio Reclamación"),  #Analisis Repo con Subsidio, tiene 2 opciones aprueba pasa a 99 y rechaza sigue el flujo #Natalia Nuñez
        ("XV_generacion_y_firma_reso_y_expediente", "1 -(Rec) Generacion y Firma Resolucion y Expediente"),  #Si es Reclamacion este es el primer paso
        ("XV_enviar_tricel", "2 -(Rec) Envío a Tricel"),
        ("XV_monitoreo", "3 -(Rec) Monitoreo Sentencia"),
        ("ABDV_remitir_abogado", "4 -(Rec) Con Sentencia en Revision Abogado"),
        ("XV", "5 -(Rec) Registro Final"),
     )
    Pago = (
        ("pendiente", "Pendiente"),
        ("con_pago", "Con Pago"),
        ("sin_pago", "Sin Pago"),
    )

    Prioridad = (
        ("Baja", "Baja"),
        ("Media", "Media"),
        ("Alta", "Alta"),
        ("Urgente - Division", "Urgente - Division"),
    )
    Celulas = (
        ("c1", "c1"),
        ("c2", "c2"),
        ("c3", "c3"),
        ("c4", "c4"),
        ("ccac_1", "ccac_1"),
        ("ccac_2", "ccac_2"),
    )
    id = models.AutoField(primary_key=True)
    tipo_recurso = models.CharField(max_length=100, null=True, blank=True)
    eleccion = models.CharField(max_length=100)
    codigotipo = models.CharField(max_length=50, default="Sin Definir")
    rut = models.IntegerField()
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)
    fecha_resolucion = models.DateField(null=True, blank=True)
    fecha_recurso = models.DateField(null=True, blank=True)
    prioridad = models.CharField(max_length=100, choices=Prioridad, default="Baja")
    estado= models.CharField(max_length=100, choices=Estados, default="Pendiente_Inicial_Ingreso_Admin")
    models.ForeignKey(UsersRecursos, on_delete=models.CASCADE, default=17311254)
    usuario_actual = models.ForeignKey(UsersRecursos, on_delete=models.CASCADE, default=17311254)
    validacion_pago = models.CharField(max_length=15, choices=Pago, default="Pendiente")
    alta_complejidad = models.BooleanField(default=False)
    celula = models.CharField(max_length=15, choices=Pago, default="Pendiente")
    link_carpeta = models.URLField(max_length=200, null=True, blank=True)
    tipo_original = models.CharField(max_length=100, null=True, blank=True)
    presentacion = models.CharField(max_length=100, null=True, blank=True)
    comentario_admin = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Bitacora(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(UsersRecursos, on_delete=models.CASCADE, default=None)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    id_recurso = models.ForeignKey(Recursos, on_delete=models.CASCADE, default=None)
    etapa = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.id

class DescripcionEstado(models.Model):
    nombre = models.CharField(max_length=200, primary_key=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.nombre

class InscripcionesPlebiscito(models.Model):

    estados_revis = (
        ("ASIGNACION", "ASIGNACION"),
        ("REVISION_AUDITOR", "REVISION_AUDITOR"),
        ("VALIDACION_ADMIN", "VALIDACION_ADMIN"),
        ("ACEPTADO", "ACEPTADO"),
        ("RECHAZADO", "RECHAZADO"),
    )
    selec_propuestas = (
        ("PENDIENTE", "PENDIENTE"),
        ("ACEPTA", "ACEPTA"),
        ("RECHAZA", "RECHAZA"),
    )
    nombre_sol = models.CharField(max_length=200, null=True, blank=True)
    paterno_sol = models.CharField(max_length=200, null=True, blank=True)
    materno_sol = models.CharField(max_length=200, null=True, blank=True)
    rut_sol = models.IntegerField()
    dv_sol = models.CharField(max_length=1)
    domicilio_sol = models.CharField(max_length=500, null=True, blank=True)
    comuna_sol = models.CharField(max_length=200, null=True, blank=True)
    telefono_fijo_sol = models.IntegerField()
    telefono_celular_sol = models.IntegerField()
    email_sol = models.CharField(max_length=200, null=True, blank=True)
    nombre_org = models.CharField(max_length=500, null=True, blank=True)
    rut_orga = models.IntegerField(null=True, blank=True)
    dv_orga = models.CharField(max_length=1, null=True, blank=True)
    domicilio_orga = models.CharField(max_length=500, null=True, blank=True)
    telefono_fijo_orga = models.IntegerField()
    telefono_celular_orga = models.IntegerField()
    email_orga = models.CharField(max_length=200, null=True, blank=True)
    id_tipo_organizacion_orga = models.IntegerField(null=True, blank=True)
    declara_fines_lucro = models.CharField(max_length=1, null=True, blank=True)
    nombre_repr = models.CharField(max_length=200, null=True, blank=True)
    paterno_repr = models.CharField(max_length=200, null=True, blank=True)
    materno_repr = models.CharField(max_length=200, null=True, blank=True)
    rut_repr = models.IntegerField()
    dv_repr = models.CharField(max_length=1)
    domicilio_repr = models.CharField(max_length=500, null=True, blank=True)
    comuna_repr = models.CharField(max_length=200, null=True, blank=True)
    telefono_fijo_repr = models.IntegerField()
    telefono_celular_repr = models.IntegerField()
    email_repr = models.CharField(max_length=500, null=True, blank=True)
    cargo_repr = models.CharField(max_length=200, null=True, blank=True)
    participara_forma = models.CharField(max_length=200, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    fecha_envio = models.DateTimeField(null=True, blank=True)
    tipo_menu = models.CharField(max_length=200, null=True, blank=True)
    id_opcion = models.CharField(max_length=200, null=True, blank=True)
    nombre_comando = models.CharField(max_length=200, null=True, blank=True)
    perjuridica = models.IntegerField(null=True, blank=True)
    organizacion = models.CharField(max_length=500, null=True, blank=True)
    tipo = models.CharField(max_length=200, null=True, blank=True)
    link_carpeta = models.URLField(max_length=200, null=True, blank=True)
    #usuario_actual_1 = models.ForeignKey(UsersRecursos, on_delete=models.CASCADE, default=17311254)
    #usuario_actual_2 = models.ForeignKey(UsersRecursos, on_delete=models.CASCADE, default=17311254)
    #usuario_actual_3 = models.ForeignKey(UsersRecursos, on_delete=models.CASCADE, default=17311254)
    etapa_revision = models.CharField(max_length=200,  choices=estados_revis, default='ASIGNACION')
    propuesta1 = models.CharField(max_length=200, choices=selec_propuestas, default='PENDIENTE')
    propuesta2 = models.CharField(max_length=200, choices=selec_propuestas, default='PENDIENTE')
    comentario_admin = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.id


from django.db import models
from datetime import datetime

class Abogados(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)
    habilitado = models.BooleanField(default=True)
    username = models.CharField(max_length=50, default='SIN')
    iniciales = models.CharField(max_length=50, default='NODEFINIDA')

    def __str__(self):
        return self.nombre


class Denuncias(models.Model):
    VIA_INGRESO = (
        ("Portal de Denuncias", "Portal de Denuncias"),
        ("División de Fiscalización", "División de Fiscalización"),
        ("Dirección Regional", "Dirección Regional"),
        ("Municipalidad", "Municipalidad"),
        ("Contraloría", "Contraloría"),
        ("Otro Órgano de la Administración del Estado", "Otro Órgano de la Administración del Estado"),
    )
    TIPO_DENUNCIADO = (
        ("Candidato", "Candidato"),
        ("Persona Natural No Candidato", "Persona Natural No Candidato"),
        ("Autoridad Pública", "Autoridad Pública"),
        ("Partido Político", "Partido Político"),
        ("Medio de Comunicación", "Medio de Comunicación"),
        ("Persona Jurídica Sin Fines de Lucro", "Persona Jurídica Sin Fines de Lucro"),
        ("Persona Jurídica Con Fines de Lucro", "Persona Jurídica Con Fines de Lucro"),
        ("Agrupación Sin Personalidad Jurídica", "Agrupación Sin Personalidad Jurídica"),
        ("Parlamentario Independiente", "Parlamentario Independiente"),
        ("Comando", "Comando"),
        ("No se puede determinar", "No se puede determinar"),
    )
    ELECCIONES = (
        ("Plebiscito", "Plebiscito"),
        ("Primarias Presidencial", "Primarias Presidencial"),
        ("Primarias Parlamentarias", "Primarias Parlamentarias"),
        ("Municipales", "Municipales"),
        ("Regionales", "Regionales"),
        ("Segunda Votación Gob. Regionales", "Segunda Votación Gob. Regionales"),
        ("Parlamentarias", "Parlamentarias"),
        ("Presidencial", "Presidencial"),
        ("Convencionales Constituyentes", "Convencionales Constituyentes"),
        ("No Aplica", "No Aplica"),

    )
    CANDIDATURA = (
        ("Nominación Alcalde", "Nominación Alcalde"),
        ("Nominación Gob. Regional", "Nominación Gob. Regional"),
        ("Alcalde", "Alcalde"),
        ("Concejal", "Concejal"),
        ("Gob. Regional", "Gob. Regional"),
        ("Consejero Regional", "Consejero Regional"),
        ("Diputado", "Diputado"),
        ("Senador", "Senador"),
        ("Pdte. de la República", "Pdte. de la República"),
        ("Convencional Constituyente", "Convencional Constituyente"),
        ("Apruebo", "Apruebo"),
        ("Rechazo", "Rechazo"),
        ("Convención Constitucional", "Convención Constitucional"),
        ("Convención Mixta", "Convención Mixta"),

    )

    MATERIA = (
        ("Financiamiento Electoral", "Financiamiento Electoral"),
        ("Gasto Electoral", "Gasto Electoral"),
        ("Rendición de Cuenta", "Rendición de Cuenta"),
        ("Medios de Comunicación", "Medios de Comunicación"),
        ("Redes Sociales", "Redes Sociales"),
        ("Espacios Públicos", "Espacios Públicos"),
        ("Espacios Privados", "Espacios Privados"),
        ("Otros Medios de Difusión", "Otros Medios de Difusión"),
        ("Otra Materia - No Competencia SCGFE", "Otra Materia - No Competencia SCGFE"),
    )
    GESTION = (
        ("Pre Instrucción", "Pre Instrucción"),
        ("Archivar", "Archivar"),
        ("Instruir Sancionador", "Instruir Sancionador"),
        ("Derivar", "Derivar"),
    )
    ASIGNACION = (
        ("Dirección Regional de Arica y Parinacota", "Dirección Regional de Arica y Parinacota"),
        ("Dirección Regional de Tarapacá", "Dirección Regional de Tarapacá"),
        ("Dirección Regional de Antofagasta", "Dirección Regional de Antofagasta"),
        ("Dirección Regional de Atacama", "Dirección Regional de Atacama"),
        ("Dirección Regional de Coquimbo", "Dirección Regional de Coquimbo"),
        ("Dirección Regional de Valparaíso", "Dirección Regional de Valparaíso"),
        ("Dirección Regional de O'Higgins", "Dirección Regional de O'Higgins"),
        ("Dirección Regional del Maule", "Dirección Regional del Maule"),
        ("Dirección Regional de Ñuble", "Dirección Regional de Ñuble"),
        ("Dirección Regional del Biobio", "Dirección Regional del Biobio"),
        ("Dirección Regional de La Araucanía", "Dirección Regional de La Araucanía"),
        ("Dirección Regional de Los Rios", "Dirección Regional de Los Rios"),
        ("Dirección Regional de Los Lagos", "Dirección Regional de Los Lagos"),
        ("Dirección Regional de Aysén", "Dirección Regional de Aysén"),
        ("Dirección Regional de Magallanes", "Dirección Regional de Magallanes"),
        ("Dirección Regional Metropolitana", "Dirección Regional Metropolitana"),
        ("División de Fiscalización", "División de Fiscalización"),
        ("Unidad de Procedimientos Administrativos Sancionatorios",
         "Unidad de Procedimientos Administrativos Sancionatorios"),
        ("Sub. Partidos Políticos", "Sub. Partidos Políticos"),
        ("Sub. Registro", "Sub. Registro"),
        ("U. Atención Ciudadana", "U. Atención Ciudadana"),
        ("Otro Órgano del Estado", "Otro Órgano del Estado"),
        ("Abogado Asistente", "Abogado Asistente"),

    )
    PLAZO = (
        ("3", "3 días"),
        ("5", "5 días"),
        ("7", "7 días"),
    )

    RESULTADO_SAD = (
        ("Aporta Nuevos Ant. Útiles", "Aporta Nuevos Ant. Útiles"),
        ("No Aporta Nuevos Ant. Útiles", "No Aporta Nuevos Ant. Útiles"),
        ("Sin Respuesta", "Sin Respuesta"),
    )
    RESULTADO_COMPROBACION = (
        ("Con Hallazgos", "Con Hallazgos"),
        ("Sin Hallazgos", "Sin Hallazgos"),
    )
    RESULTADO_CIT = (
        ("Comparece", "Comparece"),
        ("No Comparece", "No Comparece"),
     )
    RESULTADO_INSP = (
        ("Con Hallazgos", "Con Hallazgos"),
        ("Sin Hallazgos", "Sin Hallazgos"),
     )
    RESULTADO_SUB = (
        ("Subsana", "Subsana"),
        ("No Subsana", "No Subsana"),
        ("Sin Respuesta", "Sin Respuesta"),
     )
    RESULTADO_O_R = (
        ("Retira", "Retira"),
        ("No Retira", "No Retira"),
        ("Sin Respuesta", "Sin Respuesta"),
     )
    RESULTADO_ABG = (
        ("Archivar", "Archivar"),
        ("Instruir Sancionatorio", "Instruir Sancionatorio"),
        ("Derivar", "Derivar"),
     )
    Diligencias = (
        ("req_inf", "Requerimiento de Información"),
        ("sad", "SAD"),
        ("citacion", "Citación"),
        ("visita_inspectiva", "Visita Inspectiva"),
     )
    MOTIVO_ABG = (
        ("Presunta Infracción", "Presunta Infracción"),
        ("No Competencia", "No Competencia"),
        ("Falta de Mérito", "Falta de Mérito"),
        ("Falta de Plausibilidad", "Falta de Plausibilidad"),
        ("Falta de Seriedad", "Falta de Seriedad"),
     )
    ESTADO = (
        ("INGRESO", "INGRESO"),
        ("CLASIFICADO", "CLASIFICADO"),
        ("ENVIADO_JEFE", "ENVIADO_JEFE"),
        ("GEST_INGRESO_ABOGADO_REALIZADA", "GEST_INGRESO_ABOGADO_REALIZADA"),
        ("DESACTIVADO_ENVIADO_ABOGADO", "DESACTIVADO_ENVIADO_ABOGADO"),
        ("RESULTADO_ABOGADO_INGRESADO", "RESULTADO_ABOGADO_INGRESADO"),
        ("RESULTADO_ACEPTADO", "Aceptado"),
        ("RESULTADO_RECHAZADO", "Rechazado"),
        ("RESULTADO_ADMINISTRADOR", "Enviado a Administrador"),
        ("RESULTADO_ABOGADO_DEVUELTO", "Devuelto a Abogado"),
        ("RESULTADO_FINALIZADO", "Finalizado Administrador"),
     )

    INFRACCIONES = (
        ("A1", "A1"),
        ("A2", "A2"),
        ("A3", "A3"),
        ("A4", "A4"),
        ("A5", "A5"),
        ("P1", "P1"),
        ("P2", "P2"),
        ("P3", "P3"),
        ("P4", "P4"),
        ("P5", "P5"),
        ("P5-B", "P5-B"),
        ("P5-C", "P5-C"),
        ("P5-D", "P5-D"),
        ("P6", "P6"),
        ("P6-B", "P6-B"),
        ("P7", "P7"),
        ("P8", "P8"),
        ("P9", "P9"),
        ("P10", "P10"),
        ("P11", "P11"),
        ("P12", "P12"),
        ("P12-B", "P12-B"),
        ("P13", "P13"),
        ("P14", "P14"),
        ("P15", "P15"),
        ("P16", "P16"),
        ("P17", "P17"),
        ("P18", "P18"),
        ("P19", "P19"),
        ("P20", "P20"),
        ("P21", "P21"),
        ("P22", "P22"),
        ("P23", "P23"),
        ("P24", "P24"),
        ("P25", "P25"),
        ("P26", "P26"),
        ("G1", "G1"),
        ("Null", "Null"),
    )

    DESACTIVACIONES = (
        ("A1", "A1"),
        ("A2", "A2"),
        ("A3", "A3"),
        ("A4", "A4"),
        ("A5", "A5"),
        ("A6", "A6"),
        ("A7", "A7"),
        ("A8", "A8"),
        ("A9", "A9"),
        ("A10", "A10"),
        ("A11", "A11"),
        ("A12", "A12"),
        ("A13", "A13"),
        ("A14", "A14"),
        ("A15", "A15"),
        ("A16", "A16"),
        ("A17", "A17"),
        ("A18", "A18"),
        ("A19", "A19"),
        ("A20", "A20"),
        ("A21", "A21"),
        ("A22", "A22"),
        ("Null", "Null"),
    )

    numero = models.CharField(max_length=200)
    fecha_ingreso_registro = models.DateField(auto_now_add=True)
    fecha_evaluacion_abogado = models.DateField(null=True, blank=True)
    fecha_ingreso = models.DateField(default=datetime.today)
    via_de_ingreso = models.CharField(max_length=50,
                             choices=VIA_INGRESO,
                             null=True, blank=True)
    nombre_denunciante = models.CharField(max_length=200)
    nombre_denunciado = models.CharField(max_length=200)
    tipo_de_denunciado = models.CharField(max_length=50,
                             choices=TIPO_DENUNCIADO,
                             null=True, blank=True)
    elecciones = models.CharField(max_length=50,
                             choices=ELECCIONES,
                             null=True, blank=True)
    candidatura = models.CharField(max_length=50,
                             choices=CANDIDATURA,
                             null=True, blank=True)
    link_adjuntos = models.CharField(max_length=500, null=True, blank=True)

    tipo_diligencia = models.CharField(max_length=50,
                             choices=Diligencias,
                             null=True, blank=True)

    territorio_electoral = models.CharField(max_length=200)
    materia = models.CharField(max_length=50,  choices=MATERIA, null=True, blank=True)
    infraccion_denunciada = models.CharField(max_length=200, choices=INFRACCIONES, null=True, blank=True)
    gestion = models.CharField(max_length=50,  choices=GESTION, default="Pendiente")
    asignacion = models.CharField(max_length=100,  choices=ASIGNACION, default="Pendiente")

    resultado_comprobacion = models.CharField(max_length=50, choices=RESULTADO_COMPROBACION, null=True, blank=True)

    fecha_comprobacion_abogado = models.DateField(null=True, blank=True)
    guarda = models.CharField(max_length=3, default="NO")
    guardac = models.CharField(max_length=3, default="NO")
    guarda_evaluacion = models.BooleanField(default=False)
    fecha_requer = models.DateField(null=True, blank=True)
    plazo_investigacion = models.CharField(max_length=50,  choices=PLAZO, null=True, blank=True)
    abogado_asistente = models.ForeignKey(Abogados, on_delete=models.SET_NULL, null=True)

    resultado_abogado = models.CharField(max_length=50, choices=RESULTADO_ABG, null=True, blank=True)
    motivo_abogado = models.CharField(max_length=50, choices=MOTIVO_ABG, null=True, blank=True)
    estado_jefe = models.CharField(max_length=50, choices=ESTADO, default='INGRESO')
    obs_ingreso = models.TextField(null=True, blank=True)
    obs_jefe = models.TextField(null=True, blank=True)
    obs_abogado = models.TextField(null=True, blank=True)
    codigo_desactivacion = models.CharField(max_length=200, choices=DESACTIVACIONES,null=True, blank=True)

    def __str__(self):
        return self.numero

class Adjuntos(models.Model):
    id = models.AutoField(primary_key=True)
    id_denuncia = models.ForeignKey(Denuncias, on_delete=models.CASCADE, default=1)
    archivos = models.FileField(upload_to='respaldos_denuncias/', blank=True, null=True)
    tipo = models.CharField(max_length=100, default='adjunto_denuncia', blank=True, null=True)
    activo = models.BooleanField(default=True)

class Ire(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)
    eleccion = models.CharField(max_length=200)
    partido = models.CharField(max_length=200)
    pacto = models.CharField(max_length=200)
    territorio = models.CharField(max_length=200)
    celula_asignada = models.CharField(max_length=100, blank=True, null=True)


class Aportes(models.Model):
    folio = models.IntegerField(primary_key=True)
    rut_aportante = models.CharField(max_length=100,blank=True, null=True)
    nombre_aportante = models.CharField(max_length=200, null=True, blank=True)
    rut_receptor = models.ForeignKey(Ire, on_delete=models.CASCADE, default=1)
    tipo_aporte = models.CharField(max_length=200)
    fecha_abono = models.DateField(null=True, blank=True)
    fecha_recaudacion = models.DateField(null=True, blank=True)
    monto = models.IntegerField(null=True, blank=True)


class Auditores(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)
    habilitado = models.BooleanField(default=True)
    username = models.CharField(max_length=50, default='SIN')
    iniciales = models.CharField(max_length=50, default='NODEFINIDA')


class Cartola(models.Model):
    rut = models.ForeignKey(Ire, on_delete=models.CASCADE, default=1)
    dv = models.CharField(max_length=1)
    tipo = models.CharField(max_length=3)
    cuenta = models.CharField(max_length=100)
    fecemi = models.IntegerField()
    ncart = models.IntegerField()
    carr = models.IntegerField()
    numdoc = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    ofi = models.IntegerField()
    salcargos = models.IntegerField(null=True, blank=True)
    salabonos = models.IntegerField(null=True, blank=True)
    fmov = models.DateField(null=True, blank=True)
    saldo = models.IntegerField(null=True, blank=True)
    tc = models.IntegerField(null=True, blank=True)


class Formulariosig(models.Model):
    fecha_documento = models.DateField(null=True, blank=True)
    glosa = models.CharField(max_length=500, null=True, blank=True)
    monto = models.IntegerField(null=True, blank=True)
    numero_documento = models.CharField(max_length=100,null=True, blank=True)
    rut = models.IntegerField(null=True, blank=True)
    digito_verificador = models.CharField(max_length=10,null=True, blank=True)
    nombres = models.CharField(max_length=300,null=True, blank=True)
    tpo_cta_codigo = models.IntegerField(null=True, blank=True)
    tpo_doc_codigo = models.CharField(max_length=300,null=True, blank=True)
    tpo_reembolso_codigo = models.CharField(max_length=10, null=True, blank=True)
    linea = models.IntegerField(null=True, blank=True)
    pagina = models.IntegerField(null=True, blank=True)
    nombre_tpo_cta_codigo  = models.CharField(max_length=300, null=True, blank=True)
    nombre_tpo_doc_codigo  = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateField(null=True, blank=True)
    edit = models.DateField(null=True, blank=True)
    rut_partido_candidato = models.ForeignKey(Ire, on_delete=models.CASCADE, default=1)
    tipo_eleccion = models.IntegerField(null=True, blank=True)
    digito_verificador_partido_candidato = models.CharField(max_length=10,null=True, blank=True)
    tpo_rendicion_codigo = models.CharField(max_length=300,null=True, blank=True)
    id_folio = models.IntegerField(null=True, blank=True)
    ren_id = models.IntegerField(null=True, blank=True)
    id_dcto_alfresco = models.CharField(max_length=300, null=True, blank=True)
    nombre_dcto_alfresco = models.CharField(max_length=300, null=True, blank=True)
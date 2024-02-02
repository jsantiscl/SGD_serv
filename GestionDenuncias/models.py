from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Abogados(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)
    habilitado = models.BooleanField(default=True)
    username = models.CharField(max_length=50, default='SIN')
    iniciales = models.CharField(max_length=50, default='NODEFINIDA')

    def __str__(self):
        return self.nombre

class DireccionesRegionales(models.Model):
    codigo = models.CharField(primary_key=True,max_length=10)
    nombre_dr = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.nombre_dr


class EncargadosRegionales(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, default= None)
    dr_asignada = models.ForeignKey(DireccionesRegionales, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.id_usuario.username


class Denuncias(models.Model):
    VIA_INGRESO = (
        ("Cruce aportes declarados", "Cruce aportes declarados"),
        ("Reporte admisible DR", "Reporte admisible DR"),
        ("Levantamiento Meta", "Levantamiento Meta"),
        ("Otro-indicar en descripción", "Otro-indicar en descripción"),
        ("Cruce declaración medios", "Cruce declaración medios"),
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
        ("Plebiscito-Apruebo", "Plebiscito-Apruebo"),
        ("Plebiscito-Rechazo", "Plebiscito-Rechazo"),
        ("Consejero Regional", "Consejero Regional"),
        ("Plebiscito", "Plebiscito"),
        ("Primarias Presidencial", "Primarias Presidencial"),
        ("Primarias Parlamentarias", "Primarias Parlamentarias"),
        ("Municipales", "Municipales"),
        ("Regionales", "Regionales"),
        ("Segunda Votación Gob. Regionales", "Segunda Votación Gob. Regionales"),
        ("Parlamentarias", "Parlamentarias"),
        ("Presidencial", "Presidencial"),
        ("Convencionales Constituyentes", "Convencionales Constituyentes"),
        ("Consejo Constitucional 2023", "Consejo Constitucional 2023"),
        ("Plebiscito 2023", "Plebiscito 2023"),
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
        ("Plebiscito 2023", "Plebiscito 2023"),
        ("No Aplica", "No Aplica"),
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
    dr_requerimento = (
        ("Subsana", "Subsana"),
        ("No Subsana", "No Subsana"),
        ("No Responde", "No Responde"),
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
        ("EVALUADO_DR_POSIBLE_FISCALIZAR","EVALUADO_DR_POSIBLE_FISCALIZAR"),
        ("ACTIVADO_DESPACHO","ACTIVADO_DESPACHO"),
        ("ACTIVADA_COMPROBADA_ABOGADO","ACTIVADA_COMPROBADA_ABOGADO"),
        ("EVALUADO_DR_NO_POSIBLE_FISCALIZAR","EVALUADO_DR_NO_POSIBLE_FISCALIZAR"),
        ("INGRESO","INGRESO"),
        ("FISCALIZADO_DR","FISCALIZADO_DR"),
        ("GEST_INGRESO_ABOGADO_REALIZADA","GEST_INGRESO_ABOGADO_REALIZADA"),
        ("DEVUELTO_JEFE","DEVUELTO_JEFE"),
        ("DESACTIVADO_ENVIADO_ABOGADO","DESACTIVADO_ENVIADO_ABOGADO"),
        ("DESACTIVADO_DESPACHO","DESACTIVADO_DESPACHO"),

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
        ("P3-B", "P3-B"),  #Nuevo
        ("P4", "P4"),
        ("P5", "P5"),
        ("P5-B", "P5-B"),
        ("P5-C", "P5-C"),
        # ("P5-D", "P5-D"),
        ("P6", "P6"),
        ("P6-B", "P6-B"),
        ("P7", "P7"),
        #   ("P8", "P8"),
        ("P9", "P9"),
        ("P10", "P10"),
        ("P11", "P11"),
        ("P12", "P12"),
        #    ("P12-B", "P12-B"),
        ("P13", "P13"),
        ("P14", "P14"),
        ("P15", "P15"),
        ("P16", "P16"),
        ("P17", "P17"),
        #    ("P18", "P18"),
        ("P19", "P19"),
        ("P20", "P20"),
        ("P21", "P21"),
        ("P22", "P22"),
        #    ("P23", "P23"),
        #    ("P24", "P24"),
        ("P25", "P25"),
        ("P26", "P26"),
        ("P27", "P27"),  #Nuevo
        ("P28", "P28"),  # Nuevo
        ("P29", "P29"),  # Nuevo
        ("P29-B", "P29-B"),  # Nuevo
        ("P30", "P30"),  # Nuevo
        ("P100", "P100"),  # Nuevo
        ("G1", "G1"),
        ("G2", "G2"),
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
        ("A23", "A23"),
        ("A24", "A24"),
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
    asignacion_dr = models.ForeignKey(DireccionesRegionales, on_delete=models.CASCADE, default=None, null=True, blank=True)
    motivo_dr = models.CharField(max_length=300, null=True, blank=True)
    dr_id_inspeccion_survey = models.CharField(max_length=300, null=True, blank=True)
    dr_link_carpeta_fiscalizacion = models.CharField(max_length=500, null=True, blank=True)
    dr_nro_requerimiento_candidato = models.CharField(max_length=50, null=True, blank=True)
    dr_fecha_requerimiento_candidato = models.DateField(null=True, blank=True)
    dr_resultado_requerimiento_candidato = models.CharField(max_length=200, choices=dr_requerimento, null=True, blank=True)
    dr_retiro_municipio = models.CharField(max_length=50, null=True, blank=True)
    dr_fecha_retiro_municipio = models.DateField(null=True, blank=True)
    dr_guardac = models.CharField(max_length=3, default="NO")
    dr_fecha_fiscalizacion = models.DateField(null=True, blank=True)
    dr_obs_fisca = models.CharField(max_length=300, null=True, blank=True)

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
    comentarios = models.TextField(null=True, blank=True)

    @property
    def admin(self):
        admin = self.adminelectoral_set.all().first()
        return admin
    @property
    def estadopresentacion(self):
        estado = self.estadocuenta_set.all().first()
        return estado

    @property
    def saldos(self):
        detallesaldos = self.saldoscartola_set.all().first()
        return detallesaldos


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

class AdminElectoral(models.Model):
    rut = models.IntegerField()
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)
    rut_candidato = models.ForeignKey(Ire, on_delete=models.CASCADE, default=1)

class EstadoCuenta(models.Model):
    estado = models.CharField(max_length=200)
    fecha_presentacion = models.DateField(null=True, blank=True)
    rut_candidato = models.ForeignKey(Ire, on_delete=models.CASCADE, default=1)

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

class SaldosCartola(models.Model):
    rut = models.ForeignKey(Ire, on_delete=models.CASCADE, default=1)
    abonos = models.IntegerField()
    cargos = models.IntegerField()
    saldo = models.IntegerField()



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


###1.Antecedentes

class ActasTerreno(models.Model):
    object_id = models.IntegerField(null=True, blank=True)  #
    global_id = models.CharField(max_length=255, null=True, blank=True)  #
    fecha = models.CharField(max_length=255, null=True, blank=True)  #RE
    region = models.CharField(max_length=255, null=True, blank=True)  #
    ubicacion = models.CharField(max_length=255, null=True, blank=True)  #
    comuna = models.CharField(max_length=255, null=True, blank=True)  #

    ### 2. Motivo de inspección

    seleccion_motivo_inspeccion = models.CharField(max_length=255, null=True, blank=True)  #
    indique_folio = models.CharField(max_length=255, null=True, blank=True)  #
    existe_despliegue_propaganda = models.CharField(max_length=255, null=True, blank=True)  #
    indique_otro = models.CharField(max_length=255, null=True, blank=True)  #

    ### 3.sujeto fiscalizado

    Sujeto_fiscalizado = models.CharField(max_length=255, null=True, blank=True)  #
    partido_politico_habilitado = models.CharField(max_length=255, null=True, blank=True)  #
    otro_sujeto_fiscalizado = models.CharField(max_length=255, null=True, blank=True)  #

    ### 4.opción plebiscitaria

    opcion_plebiscitaria = models.CharField(max_length=30, null=True, blank=True)

    ###5.Materia fiscalizada

    materia_fiscalizada = models.CharField(max_length=255, null=True, blank=True)
    corresponde_espacio_publico_autorizado = models.CharField(max_length=255, null=True, blank=True)
    seleccione_espacio = models.CharField(max_length=255, null=True, blank=True)
    adosada_bien_nacional = models.CharField(max_length=255, null=True, blank=True)
    nombre_bienes = models.CharField(max_length=255, null=True, blank=True)
    cantidad_elementos_propaganda_publico = models.CharField(max_length=255, null=True, blank=True)
    seleccione_tipo_espacio = models.CharField(max_length=255, null=True, blank=True)
    seleccione_lugar= models.CharField(max_length=255, null=True, blank=True)
    propaganda_excede_dimensiones = models.CharField(max_length=255, null=True, blank=True)
    indique_tipo_espacio_fiscalizado = models.CharField(max_length=255, null=True, blank=True)
    actividad_fiscalizada = models.CharField(max_length=255, null=True, blank=True)
    indique_cantidad_brigadistas_lugar = models.CharField(max_length=255, null=True, blank=True)
    otro_antecente = models.CharField(max_length=5000, null=True, blank=True)
    creation_date = models.CharField(max_length=255, null=True, blank=True)  #RE  # RE
    creator = models.CharField(max_length=255, null=True, blank=True)
    edit_date = models.CharField(max_length=255, null=True, blank=True)   # RE
    editor = models.CharField(max_length=255, null=True, blank=True)
    x_coord = models.CharField(max_length=255, null=True, blank=True)
    y_coord = models.CharField(max_length=255, null=True, blank=True)
    evidencia_fotografica = models.CharField(max_length=2000, null=True, blank=True)
    link_firma_cargo_timbre = models.CharField(max_length=2000, null=True, blank=True)
    id_inspeccion = models.CharField(max_length=255, null=True, blank=True)
    CLASIFICACIONES = (
        ("Pendiente", "Pendiente"),
        ("con_infraccion_revisor_remota", "Con Infracción - Revisor Remota"),
        ("archivo_remota", "Archivo - Remota"),
        ("con_infraccion_revisor_terreno", "Con Infracción - Revisor Terreno"),
        ("archivo_terreno", "Archivo - Terreno"),
        ("EFR_Validacion", "Validación EFR"),
        ("efr_aceptado", "EFR Aceptado"),
        ("revisor_rechazo", "Rechazo EFR - Revisor"),
        ("asignado_Abogado", "Asignado a Abogado"),
        ("abogado_activado", "Activado Abogado"),
        ("abogado_devuelto", "Devuelto a DR por Abogado"),
        ("abogado_desactivado", "Desactivado Abogado"),
        ("abogado_con_infraccion", "Abogado con Infracción"),
        ("abogado_sin_infraccion", "Abogado sin Infracción"),
        ("acepta_encargado", "Acepta Encargado"),
        ("rechaza_encargado", "Rechaza Encargado"),
    )
    sis_clasificacion = models.CharField(max_length=300, default="Pendiente", choices=CLASIFICACIONES)
    CODIGOS = (
        ("p1", "P1"),
        ("p2", "P2"),
        ("p3", "P3"),
        ("p3-b", "P3-B"),
        ("p4", "P4"),
        ("p5", "P5"),
        ("p5-b", "P5-B"),
        ("p5-c", "P5-C"),
        ("p6", "P6"),
        ("p6-b", "P6-B"),
        ("p7", "P7"),
        ("p9", "P9"),
        ("p10", "P10"),
        ("p11", "P11"),
        ("p12", "P12"),
        ("p13", "P13"),
        ("p14", "P14"),
        ("p15", "P15"),
        ("p16", "P16"),
        ("p17", "P17"),
        ("p19", "P19"),
        ("p20", "P20"),
        ("p21", "P21"),
        ("p22", "P22"),
        ("p25", "P25"),
        ("p26", "P26"),
        ("p27", "P27"),
        ("p28", "P28"),
        ("p29", "P29"),
        ("p29-b", "P29-B"),
        ("p30", "P30"),
        ("p100", "P100")

    )
    sis_codigo = models.CharField(max_length=300, null=True, blank=True, choices=CODIGOS)
    sis_link = models.CharField(max_length=1000, null=True, blank=True) #ok
    sis_nro_requerimiento = models.CharField(max_length=300, null=True, blank=True) #ok
    sis_fe_sub = models.DateField(null=True, blank=True) #ok
    sis_plazo_respuesta = models.DateField(null=True, blank=True)  # ok
    sis_respuesta = models.CharField(max_length=5000, null=True, blank=True) #ok
    sis_oficio_retiro = models.CharField(max_length=1000, null=True, blank=True) #ok
    sis_certificado = models.CharField(max_length=5000, null=True, blank=True) #ok
    PROPUESTA = (
        ("Pendiente", "Pendiente"),
        ("Con Infraccion", "Con Infraccion"),
        ("Sin Infraccion", "Sin Infraccion")

    )
    sis_propuesta = models.CharField(max_length=300, default="Pendiente", choices=PROPUESTA) #ok
    sis_motivo= models.CharField(max_length=5000, null=True, blank=True) #ok
    RESULTADOEFR = (
        ("Pendiente", "Pendiente"),
        ("Acepta", "Acepta"),
        ("Rechaza", "Rechaza")

    )
    sis_resultado_efr = models.CharField(max_length=300, default="Pendiente", choices=RESULTADOEFR) #ok
    sis_motivo_rechazo = models.CharField(max_length=5000, null=True, blank=True) #ok
    sis_motivo_inicial = models.CharField(max_length=5000, null=True, blank=True)  # ok
    ABOGADOAS = (
        (16749632, "maburto"),
        (16835392, "mramirezo"),
        (17995568, "nbarraza"),
        (17051087, "dguevara"),
        (16964946, "fundurraga")
    )

    abogado_asignado = models.IntegerField(null=True, blank=True, choices=ABOGADOAS)  #
    ELECCIONES = (
        ("Plebiscito Constitucional 2023 - A Favor", "Plebiscito Constitucional 2023 - A Favor"),
        ("Plebiscito Constitucional 2023 - En Contra", "Plebiscito Constitucional 2023 - En Contra"),
        ("Municipales-Gore 2024", "Municipales-Gore 2024"),
        ("No Aplica", "No Aplica"),

    )
    abogado_eleccion = models.CharField(max_length=255, null=True, blank=True, choices=ELECCIONES)
    abogado_presunto_infractor = models.CharField(max_length=500, null=True, blank=True)
    abogado_codigo_activa = models.CharField(max_length=300, null=True, blank=True, choices=CODIGOS)
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
        ("A23", "A23"),
        ("A24", "A24"),
        ("Null", "Null"),
    )
    abogado_codigo_desactiva = models.CharField(max_length=300, null=True, blank=True, choices=DESACTIVACIONES)
    abogado_obs = models.CharField(max_length=5000, null=True, blank=True)  # ok
    abogado_motivo_devolucion = models.CharField(max_length=5000, null=True, blank=True)  # ok
    RESULTADOABOGADO = (
        ("Pendiente", "Pendiente"),
        ("Acepta", "Acepta"),
        ("Devuelve", "Devuelve")

    )
    abogado_resultado = models.CharField(max_length=300, default="Pendiente", choices=RESULTADOABOGADO)
    FINALABOGADO = (
        ("Pendiente", "Pendiente"),
        ("Con Infraccion", "Con Infraccion"),
        ("Sin Infraccion", "Sin Infraccion")

    )
    abogado_resultado_final = models.CharField(max_length=300, default="Pendiente", choices=FINALABOGADO)
    abogado_folio = models.CharField(max_length=500, null=True, blank=True)
    abogado_obs_finales = models.CharField(max_length=5000, null=True, blank=True)  # ok
    sis_encargado_resultado = models.CharField(max_length=300, default="Pendiente", choices=RESULTADOABOGADO)
    sis_motivo_rechazo_encargado = models.CharField(max_length=5000, null=True, blank=True)  # ok
    def __str__(self):
        return str(self.id_inspeccion)

class Tokens(models.Model):
    Token = models.CharField(max_length=1000, null=True, blank=True)
    Fecha = models.DateTimeField(null=True, blank=True)

### Actas remotas:
class ActasRemotas(models.Model):

    ### 1. Antecedentes
    object_id = models.IntegerField(null=True, blank=True)
    global_id = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.CharField(max_length=255, null=True, blank=True)  #RE
    region = models.CharField(max_length=255, null=True, blank=True)
    seleccion_motivo_inspeccion = models.CharField(max_length=255, null=True, blank=True)  #
    indique_folio = models.CharField(max_length=255, null=True, blank=True)  #
    indique_otro = models.CharField(max_length=255, null=True, blank=True)  #

    ### 2.sujeto fiscalizado

    sujeto_fiscalizado = models.CharField(max_length=255, null=True, blank=True)
    partido_politico_habilitado = models.CharField(max_length=255, null=True, blank=True)  #
    otro_sujeto_fiscalizado = models.CharField(max_length=255, null=True, blank=True)  #
    opcion_plebiscitaria = models.CharField(max_length=30, null=True, blank=True)

    ### 3.Materia fiscalizada

    es_medio_pagado = models.CharField(max_length=255, null=True, blank=True)
    medio_fiscalizado = models.CharField(max_length=255, null=True, blank=True)
    nombre_medio = models.CharField(max_length=255, null=True, blank=True)
    soporte_material_link = models.CharField(max_length=500, null=True, blank=True)
    medio_tiene_tarifario = models.CharField(max_length=500, null=True, blank=True)

    radiofrecuencia_medio = models.CharField(max_length=500, null=True, blank=True)
    rrss_fiscalizada = models.CharField(max_length=255, null=True, blank=True)

    usuario_perfil_rrss = models.CharField(max_length=500, null=True, blank=True)

    corresponde_medio_prensa = models.CharField(max_length=255, null=True, blank=True)
    otro_antecente = models.CharField(max_length=5000, null=True, blank=True)
    medios_respaldo_adjunto = models.CharField(max_length=2000, null=True, blank=True)
    ingrese_audios = models.CharField(max_length=2000, null=True, blank=True)
    link_firma_cargo_timbre = models.CharField(max_length=2000, null=True, blank=True)

    id_inspeccion = models.CharField(max_length=255, null=True, blank=True)
    id_workforce = models.CharField(max_length=255, null=True, blank=True)
    creation_date = models.CharField(max_length=255, null=True, blank=True)  #RE # RE
    creator = models.CharField(max_length=255, null=True, blank=True)
    edit_date = models.CharField(max_length=255, null=True, blank=True)  #RE # RE
    editor = models.CharField(max_length=255, null=True, blank=True)
    CLASIFICACIONES = (
        ("Pendiente", "Pendiente"),
        ("con_infraccion_revisor_remota", "Con Infracción - Revisor Remota"),
        ("archivo_remota", "Archivo - Remota"),
        ("con_infraccion_revisor_terreno", "Con Infracción - Revisor Terreno"),
        ("archivo_terreno", "Archivo - Terreno"),
        ("EFR_Validacion", "Validación EFR"),
        ("efr_aceptado", "EFR Aceptado"),
        ("revisor_rechazo", "Rechazo EFR - Revisor"),
        ("asignado_Abogado", "Asignado a Abogado"),
        ("abogado_activado", "Activado Abogado"),
        ("abogado_devuelto", "Devuelto a DR por Abogado"),
        ("abogado_desactivado", "Desactivado Abogado"),
        ("abogado_con_infraccion", "Abogado con Infracción"),
        ("abogado_sin_infraccion", "Abogado sin Infracción"),
        ("acepta_encargado", "Acepta Encargado"),
        ("rechaza_encargado", "Rechaza Encargado"),
    )
    sis_clasificacion = models.CharField(max_length=300, default="Pendiente", choices=CLASIFICACIONES)
    CODIGOS = (
        ("p1", "P1"),
        ("p2", "P2"),
        ("p3", "P3"),
        ("p3-b", "P3-B"),
        ("p4", "P4"),
        ("p5", "P5"),
        ("p5-b", "P5-B"),
        ("p5-c", "P5-C"),
        ("p6", "P6"),
        ("p6-b", "P6-B"),
        ("p7", "P7"),
        ("p9", "P9"),
        ("p10", "P10"),
        ("p11", "P11"),
        ("p12", "P12"),
        ("p13", "P13"),
        ("p14", "P14"),
        ("p15", "P15"),
        ("p16", "P16"),
        ("p17", "P17"),
        ("p19", "P19"),
        ("p20", "P20"),
        ("p21", "P21"),
        ("p22", "P22"),
        ("p25", "P25"),
        ("p26", "P26"),
        ("p27", "P27"),
        ("p28", "P28"),
        ("p29", "P29"),
        ("p29-b", "P29-B"),
        ("p30", "P30"),
        ("p100", "P100")

    )
    sis_codigo = models.CharField(max_length=300, null=True, blank=True, choices=CODIGOS) #ok
    sis_link = models.CharField(max_length=1000, null=True, blank=True) #ok
    sis_nro_requerimiento = models.CharField(max_length=300, null=True, blank=True) #ok
    sis_fe_sub = models.DateField(null=True, blank=True) #ok
    sis_plazo_respuesta = models.DateField(null=True, blank=True)  # ok
    sis_respuesta = models.CharField(max_length=5000, null=True, blank=True) #ok
    sis_oficio_retiro = models.CharField(max_length=1000, null=True, blank=True) #ok
    sis_certificado = models.CharField(max_length=5000, null=True, blank=True) #ok
    PROPUESTA = (
        ("Pendiente", "Pendiente"),
        ("Con Infraccion", "Con Infraccion"),
        ("Sin Infraccion", "Sin Infraccion")

    )
    sis_propuesta = models.CharField(max_length=300, default="Pendiente", choices=PROPUESTA) #ok
    sis_motivo= models.CharField(max_length=5000, null=True, blank=True) #ok
    RESULTADOEFR = (
        ("Pendiente", "Pendiente"),
        ("Acepta", "Acepta"),
        ("Rechaza", "Rechaza")

    )
    sis_resultado_efr = models.CharField(max_length=300, default="Pendiente", choices=RESULTADOEFR) #ok
    sis_motivo_rechazo = models.CharField(max_length=5000, null=True, blank=True)  # ok
    sis_motivo_inicial = models.CharField(max_length=5000, null=True, blank=True)  # ok
    ABOGADOAS = (
        (16749632, "maburto"),
        (16835392, "mramirezo"),
        (17995568, "nbarraza"),
        (17051087, "dguevara"),
        (16964946, "fundurraga")
    )

    abogado_asignado = models.IntegerField(null=True, blank=True, choices=ABOGADOAS)  #
    ELECCIONES = (
        ("Plebiscito Constitucional 2023 - A Favor", "Plebiscito Constitucional 2023 - A Favor"),
        ("Plebiscito Constitucional 2023 - En Contra", "Plebiscito Constitucional 2023 - En Contra"),
        ("Municipales-Gore 2024", "Municipales-Gore 2024"),
        ("No Aplica", "No Aplica"),

    )
    abogado_eleccion = models.CharField(max_length=255, null=True, blank=True, choices=ELECCIONES)
    abogado_presunto_infractor = models.CharField(max_length=500, null=True, blank=True)
    abogado_codigo_activa = models.CharField(max_length=300, null=True, blank=True, choices=CODIGOS)
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
        ("A23", "A23"),
        ("A24", "A24"),
        ("Null", "Null"),
    )
    abogado_codigo_desactiva = models.CharField(max_length=300, null=True, blank=True, choices=DESACTIVACIONES)
    abogado_obs = models.CharField(max_length=5000, null=True, blank=True)  # ok
    abogado_motivo_devolucion = models.CharField(max_length=5000, null=True, blank=True)  # ok
    RESULTADOABOGADO = (
        ("Pendiente", "Pendiente"),
        ("Acepta", "Acepta"),
        ("Devuelve", "Devuelve")

    )
    abogado_resultado = models.CharField(max_length=300, default="Pendiente", choices=RESULTADOABOGADO)
    FINALABOGADO = (
        ("Pendiente", "Pendiente"),
        ("Con Infraccion", "Con Infraccion"),
        ("Sin Infraccion", "Sin Infraccion")

    )
    abogado_resultado_final = models.CharField(max_length=300, default="Pendiente", choices=FINALABOGADO)
    abogado_folio = models.CharField(max_length=500, null=True, blank=True)
    abogado_obs_finales = models.CharField(max_length=5000, null=True, blank=True)  # ok
    sis_encargado_resultado = models.CharField(max_length=300, default="Pendiente", choices=RESULTADOABOGADO)
    sis_motivo_rechazo_encargado = models.CharField(max_length=5000, null=True, blank=True)  # ok
    def __str__(self):
        return str(self.id_inspeccion)

class RevisoresDR(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Region = models.CharField(max_length=50, null=True, blank=True)  # ok
    def __str__(self):
        return str(self.Region)

class EFRDR(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Region = models.CharField(max_length=50, null=True, blank=True)  # ok
    def __str__(self):
        return str(self.Region)


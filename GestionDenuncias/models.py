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
        ("Primarias", "Primarias"),
        ("Municipales", "Municipales"),
        ("Regionales", "Regionales"),
        ("Segunda Votación Gob. Regionales", "Segunda Votación Gob. Regionales"),
        ("Parlamentarias", "Parlamentarias"),
        ("Presidencial", "Presidencial"),
        ("Convencionales Constituyentes", "Convencionales Constituyentes"),

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
    RESULTADO_REQ = (
        ("Aporta Info. Requerida", "Aporta Info. Requerida"),
        ("No Aporta Info. Requerida", "No Aporta Info. Requerida"),
        ("Sin Respuesta", "Sin Respuesta"),
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

    diligencia_sad = models.BooleanField(default=False)
    fecha_sol_sad = models.DateField(null=True, blank=True)
    fecha_res_sad = models.DateField(null=True, blank=True)
    resultado_sad = models.CharField(max_length=50, choices=RESULTADO_SAD, null=True, blank=True)

    diligencia_req_inf = models.BooleanField(default=False)
    fecha_sol_req = models.DateField(null=True, blank=True)
    fecha_res_req = models.DateField(null=True, blank=True)
    resultado_req = models.CharField(max_length=50, choices=RESULTADO_REQ, null=True, blank=True)

    diligencia_citacion = models.BooleanField(default=False)
    fecha_citacion = models.DateField(null=True, blank=True)
    fecha_comparecencia = models.DateField(null=True, blank=True)
    resultado_cit = models.CharField(max_length=50, choices=RESULTADO_CIT, null=True, blank=True)

    diligencia_insp_terreno = models.BooleanField(default=False)
    fecha_inspeccion_terr = models.DateField(null=True, blank=True)
    unidad_fiscalizada_terr = models.CharField(max_length=200, null=True, blank=True)
    resultado_insp_terr = models.CharField(max_length=50, choices=RESULTADO_INSP, null=True, blank=True)

    diligencia_insp_remota = models.BooleanField(default=False)
    fecha_inspeccion_rem = models.DateField(null=True, blank=True)
    unidad_fiscalizada_rem = models.CharField(max_length=200, null=True, blank=True)
    resultado_insp_rem = models.CharField(max_length=50, choices=RESULTADO_INSP, null=True, blank=True)
    guarda = models.CharField(max_length=3, default="NO")
    guarda_evaluacion = models.BooleanField(default=False)
    fecha_inspeccion_sub = models.DateField(null=True, blank=True)
    unidad_fiscalizada_sub = models.CharField(max_length=200, null=True, blank=True)
    resultado_insp_sub = models.CharField(max_length=50, choices=RESULTADO_SUB, null=True, blank=True)

    diligencia_orden_retiro = models.BooleanField(default=False)
    fecha_requer = models.DateField(null=True, blank=True)
    municipalidad = models.CharField(max_length=200, null=True, blank=True)
    resultado_orden_ret = models.CharField(max_length=50, choices=RESULTADO_O_R, null=True, blank=True)

    diligencia_otra = models.BooleanField(default=False)

    plazo_investigacion = models.CharField(max_length=50,  choices=PLAZO, null=True, blank=True)
    abogado_asistente = models.ForeignKey(Abogados, on_delete=models.SET_NULL, null=True)

    resultado_abogado = models.CharField(max_length=50, choices=RESULTADO_ABG, null=True, blank=True)
    motivo_abogado = models.CharField(max_length=50, choices=MOTIVO_ABG, null=True, blank=True)
    estado_jefe = models.CharField(max_length=50, choices=ESTADO, default='INGRESO')
    obs_ingreso = models.TextField(null=True, blank=True)
    obs_jefe = models.TextField(null=True, blank=True)
    obs_abogado = models.TextField(null=True, blank=True)
    adjunto_denuncia = models.FileField(upload_to='respaldos_denuncias/', blank=True, null=True)
    adjunto_sol_sad = models.FileField(upload_to='SAD/SOLICITUD/', blank=True, null=True)
    adjunto_sol_req_inf = models.FileField(upload_to='REQ_INF/SOLICITUD/', blank=True, null=True)
    adjunto_sol_cit = models.FileField(upload_to='CITACION/SOLICITUD/', blank=True, null=True)
    adjunto_sol_ins_terr = models.FileField(upload_to='INSP_TERRENO/SOLICITUD/', blank=True, null=True)
    adjunto_sol_ins_rem = models.FileField(upload_to='INSP_REMOTA/SOLICITUD/', blank=True, null=True)
    adjunto_sol_req_sub = models.FileField(upload_to='REQ_SUBSANACION/SOLICITUD/', blank=True, null=True)
    adjunto_sol_ord_ret = models.FileField(upload_to='ORD_RETIRO/SOLICITUD/', blank=True, null=True)
    adjunto_res_sad = models.FileField(upload_to='SAD/RESPUESTA/', blank=True, null=True)
    adjunto_res_req_inf = models.FileField(upload_to='REQ_INF/RESPUESTA/', blank=True, null=True)
    adjunto_res_cit = models.FileField(upload_to='CITACION/RESPUESTA/', blank=True, null=True)
    adjunto_res_ins_terr = models.FileField(upload_to='INSP_TERRENO/RESPUESTA/', blank=True, null=True)
    adjunto_res_ins_rem = models.FileField(upload_to='INSP_REMOTA/RESPUESTA/', blank=True, null=True)
    adjunto_res_req_sub = models.FileField(upload_to='REQ_SUBSANACION/RESPUESTA/', blank=True, null=True)
    adjunto_res_ord_ret = models.FileField(upload_to='ORD_RETIRO/RESPUESTA/', blank=True, null=True)
    adjunto_informe = models.FileField(upload_to='INFORME/', blank=True, null=True)
    tiene_adjunto_sol_sad = models.BooleanField(default=False)
    tiene_adjunto_sol_req_inf = models.BooleanField(default=False)
    tiene_adjunto_sol_cit = models.BooleanField(default=False)
    tiene_adjunto_sol_ins_terr = models.BooleanField(default=False)
    tiene_adjunto_sol_ins_rem = models.BooleanField(default=False)
    tiene_adjunto_sol_req_sub = models.BooleanField(default=False)
    tiene_adjunto_sol_ord_ret = models.BooleanField(default=False)

    tiene_adjunto_res_sad = models.BooleanField(default=False)
    tiene_adjunto_res_req_inf = models.BooleanField(default=False)
    tiene_adjunto_res_cit = models.BooleanField(default=False)
    tiene_adjunto_res_ins_terr = models.BooleanField(default=False)
    tiene_adjunto_res_ins_rem = models.BooleanField(default=False)
    tiene_adjunto_res_req_sub = models.BooleanField(default=False)
    tiene_adjunto_res_ord_ret = models.BooleanField(default=False)
    tiene_adjunto_informe = models.BooleanField(default=False)
    codigo_desactivacion = models.CharField(max_length=200, choices=DESACTIVACIONES,null=True, blank=True)

    def __str__(self):
        return self.numero

class Adjuntos(models.Model):
    id = models.AutoField(primary_key=True)
    id_denuncia = models.ForeignKey(Denuncias, on_delete=models.CASCADE, default=1)
    archivos = models.FileField(upload_to='respaldos_denuncias/', blank=True, null=True)
    tipo = models.CharField(max_length=100, default='adjunto_denuncia', blank=True, null=True)
    activo = models.BooleanField(default=True)
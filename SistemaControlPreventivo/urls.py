from django.urls import path
from django.urls import include
from django.contrib.auth.decorators import login_required
from SistemaControlPreventivo.views import *
urlpatterns = [
    # ENCARGADO
    path('asignacioncandidatos/', login_required(admin_asignacion_candidato), name='admin_asignacion_candidato'),
    path('asignacionpartidos/', login_required(admin_asignacion_partido), name='admin_asignacion_partido'),
    path('asignacandidatos/', login_required(asignar_candidatos_scp), name='asignar_candidatos_scp'),
    path('asignapartidos/', login_required(asignar_partidos_scp), name='asignar_partidos_scp'),
    path('reportecandidato/', login_required(admin_reporte_candidato), name='admin_reporte_candidato'),
    path('reportepartido/', login_required(admin_reporte_partido), name='admin_reporte_partido'),
    # Auditor
    path('candidatos/', login_required(auditor_candidatos), name='auditor_candidatos'),
    path('candidatos/sra/<str:cod>', login_required(sra_candidatos), name='sra_candidatos'),
    path('partidos/sra/<str:cod>', login_required(sra_partidos), name='sra_partidos'),
    path('candidatos/cartolas/<str:cod>', login_required(cartola_candidatos), name='cartolas_candidatos'),
    path('partidos/cartolas/<str:cod>', login_required(cartola_partidos), name='cartolas_partidos'),
    path('partidos/', login_required(auditor_partidos), name='auditor_partidos'),
    path('pasaretapa/', login_required(pasaretapa), name='pasaretapa'),
    #Revisor
    path('revisarpartidos/', login_required(revisor_partidos_scp), name='revisor_partidos_scp'),
    path('revisarcandidatos1/', login_required(revisor_candidatos1_scp), name='revisor_candidatos1_scp'),
    path('revisarcandidatos2/', login_required(revisor_candidatos2_scp), name='revisor_candidatos2_scp'),
    path('respuestascp/', login_required(respuestas_CP), name='respuestas_CP'),
    # Abogado
    path('abogadopartido/', login_required(abogado_partidos_scp), name='abogado_partidos_scp'),
    path('abogadopartido2/', login_required(abogado_partidos_scp2), name='abogado_partidos_scp2'),
    path('abogadocandidatos/', login_required(abogado_candidatos), name='abogado_candidatos_scp'),
    path('abogadocandidatos2/', login_required(abogado_candidatos2), name='abogado_candidatos_scp2'),
    path('abogadocandidatos3/', login_required(abogado_candidatos3), name='abogado_candidatos_scp3'),
    path('abogadocandidatos4/', login_required(abogado_candidatos4), name='abogado_candidatos_scp4'),
    # Jefe Unidad
    path('jucandidatos/', login_required(jefeunidad_candidatos), name='jefeunidad_candidatos'),
    path('jupartidos/', login_required(jefeunidad_partidos), name='jefeunidad_partidos'),
    # Jefe Division
    path('jdcandidatos/', login_required(jefedivision_candidatos), name='jefedivision_candidatos'),
    path('jdpartidos/', login_required(jefedivision_partidos), name='jefedivision_partidos'),
    # Notificacion
    path('notificacioncandidatos/', login_required(notificacion_candidatos), name='notificacion_candidatos'),
    path('notificacionpartidos/', login_required(notificacion_partidos), name='notificacion_partidos'),

    #API
    path('api/nueva_respuesta/', carga_datos_respuestas, name='carga_datos_respuestas'),  # P
]

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
    path('partidos/', login_required(auditor_partidos), name='auditor_partidos'),
    path('pasaretapa/', login_required(pasaretapa), name='pasaretapa'),
    #Revisor
    path('revisarpartidos/', login_required(revisor_partidos_scp), name='revisor_partidos_scp'),
    path('revisarcandidatos1/', login_required(revisor_candidatos1_scp), name='revisor_candidatos1_scp'),
    path('revisarcandidatos2/', login_required(revisor_candidatos2_scp), name='revisor_candidatos2_scp'),
    # Abogado
    path('abogadopartido/', login_required(abogado_partidos_scp), name='abogado_partidos_scp'),
    path('abogadocandidatos/', login_required(abogado_candidatos), name='abogado_candidatos_scp'),
    path('abogadocandidatos2/', login_required(abogado_candidatos2), name='abogado_candidatos_scp2'),
    # Jefe Unidad
    path('jucandidatos/', login_required(jefeunidad_candidatos), name='jefeunidad_candidatos'),
    path('jupartidos/', login_required(jefeunidad_partidos), name='jefeunidad_partidos'),
    # Jefe Division
    path('jdcandidatos/', login_required(jefedivision_candidatos), name='jefedivision_candidatos'),
    path('jdpartidos/', login_required(jefedivision_partidos), name='jefedivision_partidos'),
    # Notificacion
    path('notificacioncandidatos/', login_required(notificacion_candidatos), name='notificacion_candidatos'),
    path('notificacionpartidos/', login_required(notificacion_partidos), name='notificacion_partidos'),
]

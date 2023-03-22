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
    # Auditor
    path('candidatos/', login_required(auditor_candidatos), name='auditor_candidatos'),
    path('partidos/', login_required(auditor_partidos), name='auditor_partidos'),
    path('pasaretapa/', login_required(pasaretapa), name='pasaretapa'),
]

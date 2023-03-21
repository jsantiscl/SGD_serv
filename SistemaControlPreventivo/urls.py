from django.urls import path
from django.urls import include
from django.contrib.auth.decorators import login_required
from SistemaControlPreventivo.views import *
urlpatterns = [
    # Fiscalizacion
    path('asignacioncandidatos/', login_required(admin_asignacion_candidato), name='admin_asignacion_candidato'),
    path('asignacionpartidos/', login_required(admin_asignacion_partido), name='admin_asignacion_partido'),
    path('asignacandidatos/', login_required(asignar_candidatos_scp), name='asignar_candidatos_scp'),
]

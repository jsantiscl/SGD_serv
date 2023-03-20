from django.shortcuts import render
from django.contrib.auth.models import User, Group
from SistemaControlPreventivo.models import *
import json
from django.http import JsonResponse
from datetime import datetime
# Create your views here.
def admin_asignacion_candidato(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='1_Ingreso')

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Admin_Asignacion.html', context)


def asignar_candidatos_scp(request):
    data = json.loads(request.body)
    if data['datos']['asignacion'] != 'Pendiente':
         Candidatos.objects.filter(rut=str(data['datos']['rut'])).update(asignado_a=str(data['datos']['asignacion']))
         Candidatos.objects.filter(rut=str(data['datos']['rut'])).update(estado='2_AsignadoAuditor')
         WorkflowSCP.objects.create(rut_candidato_partido=str(data['datos']['rut']), usuario=str(data['datos']['asignacion']),
                                                nueva_etapa='2_AsignadoAuditor',
                                                fecha_cambio=datetime.now())
    return JsonResponse([str(data['datos']['rut']), 'Asignado'], safe=False)
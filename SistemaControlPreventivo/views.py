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


def admin_asignacion_partido(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivoPP")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Filtrar los candidatos como lo hacías antes
    candidatos = Partidos.objects.filter(estado='1_Ingreso')

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Admin_Asignacion_Partidos.html', context)


def auditor_candidatos(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='2_AsignadoAuditor', asignado_a=usuario_actual)

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Auditor_Candidatos.html', context)

def auditor_partidos(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    partidos = Partidos.objects.filter(estado='2_AsignadoAuditor', asignado_a=usuario_actual)
    print(usuario_actual)
    # Agregar los auditores al contexto
    context = {'partidos': partidos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Auditor_Partidos.html', context)

def pasaretapa(request):
    data = json.loads(request.body)
    if data['datos']['tipo'] == 'Candidato':
         Candidatos.objects.filter(rut=str(data['datos']['rut'])).update(estado=str(data['datos']['etapa']))
         WorkflowSCP.objects.create(rut_candidato_partido=str(data['datos']['rut']), usuario=str(request.user),
                                                nueva_etapa=str(data['datos']['etapa']),
                                                fecha_cambio=datetime.now())
    if data['datos']['tipo'] == 'Partido':
         Partidos.objects.filter(par_rut=str(data['datos']['rut'])).update(estado=str(data['datos']['etapa']))
         WorkflowSCP.objects.create(rut_candidato_partido=str(data['datos']['rut']), usuario=str(request.user),
                                                nueva_etapa=str(data['datos']['etapa']),
                                                fecha_cambio=datetime.now())
    return JsonResponse([str(data['datos']['rut']), 'Asignado'], safe=False)

def asignar_partidos_scp(request):
    data = json.loads(request.body)
    if data['datos']['asignacion'] != 'Pendiente':
         Partidos.objects.filter(par_rut=str(data['datos']['rut'])).update(asignado_a=str(data['datos']['asignacion']))
         Partidos.objects.filter(par_rut=str(data['datos']['rut'])).update(estado='2_AsignadoAuditor')
         WorkflowSCP.objects.create(rut_candidato_partido=str(data['datos']['rut']), usuario=str(data['datos']['asignacion']),
                                                nueva_etapa='2_AsignadoAuditor',
                                                fecha_cambio=datetime.now())
    return JsonResponse([str(data['datos']['rut']), 'Asignado'], safe=False)


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


def revisor_partidos_scp(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    partidos = Partidos.objects.filter(estado='3_EnRevisor')

    # Agregar los auditores al contexto
    context = {'partidos': partidos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Revisor_Partidos.html', context)

def abogado_partidos_scp(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    partidos = Partidos.objects.filter(estado='4_ConHallazgosAbogado')

    # Agregar los auditores al contexto
    context = {'partidos': partidos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Abogado_Partidos.html', context)

def admin_reporte_candidato(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.all()

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Admin_ReporteCandidatos.html', context)

def admin_reporte_partido(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Filtrar los candidatos como lo hacías antes
    partidos = Partidos.objects.all()

    # Agregar los auditores al contexto
    context = {'partidos': partidos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Admin_Reporte_Partidos.html', context)


def revisor_candidatos1_scp(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="1")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Obtener una lista de nombres de usuario de auditores
    nombres_auditores = [auditor.username for auditor in auditores]

    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='3_EnRevisor', asignado_a__in=nombres_auditores)

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Revisor_Candidatos1.html', context)


def revisor_candidatos2_scp(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="2")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Obtener una lista de nombres de usuario de auditores
    nombres_auditores = [auditor.username for auditor in auditores]

    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='3_EnRevisor', asignado_a__in=nombres_auditores)

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Revisor_Candidatos2.html', context)

def abogado_candidatos(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='4_ConHallazgosAbogado')

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Abogado_Candidatos.html', context)

def jefeunidad_candidatos(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='5_EnJefeUnidad')

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_JUnidad_Candidatos.html', context)

def jefedivision_candidatos(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='6_JefeDivision')

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_JDivision_Candidatos.html', context)


def notificacion_candidatos(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='7_EnNotificacion')

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Notificacion_Candidatos.html', context)


def jefeunidad_partidos(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    candidatos = Partidos.objects.filter(estado='5_EnJefeUnidad')

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_JUnidad_Partidos.html', context)

def jefedivision_partidos(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    candidatos = Partidos.objects.filter(estado='6_JefeDivision')

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_JDivision_Partidos.html', context)


def notificacion_partidos(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    candidatos = Partidos.objects.filter(estado='7_EnNotificacion')

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Notificacion_Partidos.html', context)

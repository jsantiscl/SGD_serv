from django.shortcuts import render
from django.contrib.auth.models import User, Group
from SistemaControlPreventivo.models import *
import json
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

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
    usuario_actual = request.user.username

    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='2_AsignadoAuditor', asignado_a=usuario_actual)

    # Agregar el campo 'cod' a los candidatos
    candidatos_cod = []
    for candidato in candidatos:
        cod_rel_candidato = rel_candidato.objects.filter(rut=candidato.rut).first()
        if cod_rel_candidato:
            candidato.cod = cod_rel_candidato.cod
        else:
            candidato.cod = None
        candidatos_cod.append(candidato)

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos_cod, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Auditor_Candidatos.html', context)
def auditor_partidos(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    partidos = Partidos.objects.filter(estado='2_AsignadoAuditor', asignado_a=usuario_actual)
    # Agregar el campo 'cod' a los candidatos
    candidatos_cod = []
    for partido in partidos:
        cod_rel_candidato = rel_partido.objects.filter(rut=partido.par_rut).first()
        if cod_rel_candidato:
            partido.cod = cod_rel_candidato.cod
        else:
            partido.cod = None
        candidatos_cod.append(partido)
    # Agregar los auditores al contexto
    context = {'partidos': partidos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Auditor_Partidos.html', context)

def pasaretapa(request):
    data = json.loads(request.body)
    if data['datos']['respuesta'] == None:
        respuesta = ''
    if data['datos']['respuesta'] != None:
        respuesta = data['datos']['respuesta']
    if data['datos']['tipo'] == 'Candidato':
         Candidatos.objects.filter(rut=str(data['datos']['rut'])).update(estado=str(data['datos']['etapa']), observacion_rechazo=respuesta)
         WorkflowSCP.objects.create(rut_candidato_partido=str(data['datos']['rut']), usuario=str(request.user),
                                                nueva_etapa=str(data['datos']['etapa']),
                                                fecha_cambio=datetime.now())
    if data['datos']['tipo'] == 'Partido':
         Partidos.objects.filter(par_rut=str(data['datos']['rut'])).update(estado=str(data['datos']['etapa']), observacion_rechazo=respuesta)
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
    group = Group.objects.get(name="1")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Obtener una lista de nombres de usuario de auditores
    nombres_auditores = [auditor.username for auditor in auditores]

    # Filtrar los candidatos como lo hacías antes
    partidos = Partidos.objects.filter(estado='4_ConHallazgosAbogado', asignado_a__in=nombres_auditores)

    # Agregar los auditores al contexto
    context = {'partidos': partidos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Abogado_Partidos.html', context)

def abogado_partidos_scp2(request):
    group = Group.objects.get(name="2")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Obtener una lista de nombres de usuario de auditores
    nombres_auditores = [auditor.username for auditor in auditores]

    # Filtrar los candidatos como lo hacías antes
    partidos = Partidos.objects.filter(estado='4_ConHallazgosAbogado', asignado_a__in=nombres_auditores)

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
    group = Group.objects.get(name="a")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Obtener una lista de nombres de usuario de auditores
    nombres_auditores = [auditor.username for auditor in auditores]

    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='4_ConHallazgosAbogado', asignado_a__in=nombres_auditores)

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Abogado_Candidatos.html', context)

def abogado_candidatos2(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="b")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Obtener una lista de nombres de usuario de auditores
    nombres_auditores = [auditor.username for auditor in auditores]

    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='4_ConHallazgosAbogado', asignado_a__in=nombres_auditores)

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Abogado_Candidatos.html', context)

def abogado_candidatos3(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="c")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Obtener una lista de nombres de usuario de auditores
    nombres_auditores = [auditor.username for auditor in auditores]

    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='4_ConHallazgosAbogado', asignado_a__in=nombres_auditores)

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Abogado_Candidatos.html', context)

def abogado_candidatos4(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="d")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Obtener una lista de nombres de usuario de auditores
    nombres_auditores = [auditor.username for auditor in auditores]

    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='4_ConHallazgosAbogado', asignado_a__in=nombres_auditores)

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


def sra_candidatos(request,cod):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    candidato = rel_candidato.objects.filter(cod__exact=cod).first()
    # Filtrar los candidatos como lo hacías antes
    aportes = AportesSRA.objects.filter(rut_candidato_o_partido__icontains=candidato.rut).exclude(estado_servel='APORTE NO EFECTUADO')

    # Agregar los auditores al contexto
    context = {'aportes': aportes, 'auditores': auditores, 'candidato':candidato.rut}

    return render(request, 'SistemaControlPreventivo/SCP_SRA.html', context)

def sra_partidos(request,cod):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    partido = rel_partido.objects.filter(cod__exact=cod).first()
    # Filtrar los candidatos como lo hacías antes
    aportes = AportesSRA.objects.filter(rut_candidato_o_partido__icontains=partido.rut).exclude(estado_servel='APORTE NO EFECTUADO')

    # Agregar los auditores al contexto
    context = {'aportes': aportes, 'auditores': auditores, 'candidato':partido.rut}

    return render(request, 'SistemaControlPreventivo/SCP_SRA.html', context)

def cartola_candidatos(request,cod):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    candidato = rel_candidato.objects.filter(cod__exact=cod).first()
    # Filtrar los candidatos como lo hacías antes
    cartolas = Cartolas.objects.filter(rut=candidato.rut)

    # Agregar los auditores al contexto
    context = {'cartolas': cartolas, 'auditores': auditores, 'candidato':candidato.rut}

    return render(request, 'SistemaControlPreventivo/SCP_Cartolas.html', context)

def cartola_partidos(request,cod):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    partido = rel_partido.objects.filter(cod__exact=cod).first()
    # Filtrar los candidatos como lo hacías antes
    cartolas = Cartolas.objects.filter(rut=partido.rut)

    # Agregar los auditores al contexto
    context = {'cartolas': cartolas, 'auditores': auditores, 'candidato':partido.rut}

    return render(request, 'SistemaControlPreventivo/SCP_Cartolas.html', context)


def respuestas_CP(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()
    usuario_actual=request.user.username
    # Filtrar los candidatos como lo hacías antes
    respuestas = RespuestasCP.objects.filter(Etapa='1_Nueva')

    # Obtener el token con el mayor ID
    try:
        latest_token = Tokens.objects.latest('id')
    except ObjectDoesNotExist:
        latest_token = None

    # Agregar los auditores y el token al contexto
    context = {'respuestas': respuestas, 'auditores': auditores, 'latest_token': latest_token}

    return render(request, 'SistemaControlPreventivo/SCP_Respuestas_Revisor.html', context)


@csrf_exempt
def carga_datos_respuestas(request):
    if request.method == 'POST':
        # Extrae los datos de la solicitud POST
        ObjectID = request.POST.get('ObjectID')
        GlobalID = request.POST.get('GlobalID')
        NombreCompleto = request.POST.get('NombreCompleto')
        Rut = request.POST.get('Rut')
        TemaAsociado = request.POST.get('TemaAsociado')
        Pregunta = request.POST.get('Pregunta')
        Email = request.POST.get('Email')
        Adjunto = request.POST.get('Adjunto')
        # Crea una instancia de tu modelo de datos y asigna los valores de la solicitud POST
        data = RespuestasCP(ObjectID=ObjectID,
                                   GlobalID=GlobalID,
                                   NombreCompleto=NombreCompleto,
                                   Rut=Rut,
                                   TemaAsociado=TemaAsociado,
                                   Pregunta=Pregunta,
                                   Email=Email,
                                   FechaIngreso=datetime.now(),
                                   Etapa='1_Nueva',
                                   Adjunto = Adjunto)

        # Guarda la instancia en la base de datos
        data.save()

        # Retorna una respuesta HTTP 200 si
        return HttpResponse('Datos guardados correctamente')
    else:
        # Retorna una respuesta HTTP 405 si se recibe una solicitud que no es POST
        return HttpResponse(status=405)
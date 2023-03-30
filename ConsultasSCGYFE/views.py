from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from django.db.models import Count
from GestionRecursos.models import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404
# Create your views here.

from django.conf import settings
from django.core.mail import send_mail
from ConsultasSCGYFE.models import *

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def admin_consultas_total(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = ConsultasFormulario.objects.all()
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'Consultas/Consultas.html', context)

def consultas_nuevas(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like

    if request.user.groups.filter(name='Consultas_Financiamiento').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="1_Nueva",
                                                            TemaAsociado__icontains="financiamiento")
    elif request.user.groups.filter(name='Consultas_Propaganda').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="1_Nueva",
                                                            TemaAsociado__icontains="propaganda")
    elif request.user.groups.filter(name='Consultas_AdministracionE').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="1_Nueva",
                                                            TemaAsociado__icontains="administracion")
    elif request.user.groups.filter(name='Consultas_Contabilidad').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="1_Nueva",
                                                            TemaAsociado__icontains="contabilidad")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'Consultas/Consultas_Nuevas.html', context)

def consultas_pasar_etapa(request):
    data = json.loads(request.body)
    ConsultasFormulario.objects.filter(ObjectID=int(data['datos']['ObjectID'])).update(Etapa=str(data['datos']['etapa']), RespondidoPor=request.user.username)
    objeto = ConsultasFormulario.objects.filter(ObjectID=int(data['datos']['ObjectID']))
    WorkflowConsultas.objects.create(ObjectID=objeto[0].ObjectID, GlobalID=objeto[0].GlobalID, Usuario = request.user.username, NuevaEtapa = str(data['datos']['etapa']), FechaCambio = datetime.now())
    return JsonResponse([str(data['datos']['ObjectID']), 'Pasa'], safe=False)


def consultas_respuesta(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like

    denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="2_Respuesta")
    context = {'todasdenuncias': denuncia_obj_3, 'user': request.user}
    return render(request,'Consultas/Consultas_Respuesta.html', context)

def consultas_responder(request):
    data = json.loads(request.body)
    ConsultasFormulario.objects.filter(ObjectID=int(data['datos']['ObjectID'])).update(Etapa=str(data['datos']['etapa']), Respuesta=str(data['datos']['respuesta']), Email=str(data['datos']['email']), Fecha_Respuesta=datetime.now(), Respondido=str(data['datos']['respondido']))
    objeto = ConsultasFormulario.objects.filter(ObjectID=int(data['datos']['ObjectID']))
    WorkflowConsultas.objects.create(ObjectID=objeto[0].ObjectID, GlobalID=objeto[0].GlobalID, Usuario = request.user.username, NuevaEtapa = str(data['datos']['etapa']), FechaCambio = datetime.now())
    return JsonResponse([str(data['datos']['ObjectID']), 'Pasa'], safe=False)

def consultas_envio_respuestas(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like

    denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="3_Resuelta")
    context = {'todasdenuncias': denuncia_obj_3, 'user': request.user}
    return render(request,'Consultas/Consultas_Envio_Respuesta.html', context)


def consultas_respondidas(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like

    denuncia_obj_3 = ConsultasFormulario.objects.filter(Q(Etapa__icontains="2_Respuesta") | Q(Etapa__icontains="3_Resuelta")| Q(Etapa__icontains="4_Enviada"))
    context = {'todasdenuncias': denuncia_obj_3, 'user': request.user}
    return render(request,'Consultas/Consultas_Respondidas.html', context)


def sandbox(request):

    context = {}
    return render(request,'Consultas/Sandbox.html', context)


@csrf_exempt
def carga_datos_consulta(request):
    if request.method == 'POST':
        # Extrae los datos de la solicitud POST
        rut_org = request.POST.get('rut_org')
        id_org = request.POST.get('id_org')
        rut_socio = request.POST.get('rut_socio')

        # Crea una instancia de tu modelo de datos y asigna los valores de la solicitud POST
        data = SociosInscritos(id =rut_org, rut_org=rut_org, id_org=id_org, rut_socio=rut_socio)

        # Guarda la instancia en la base de datos
        data.save()

        # Retorna una respuesta HTTP 200 si
        return HttpResponse('Datos guardados correctamente')
    else:
        # Retorna una respuesta HTTP 405 si se recibe una solicitud que no es POST
        return HttpResponse(status=405)
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


def admin_consultas_total(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = ConsultasFormulario.objects.all()
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'Consultas/Consultas.html', context)

def consultas_nuevas(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like

    if request.user.groups.filter(name='Consultas_Financiamiento').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="1_Nueva",
                                                            TemaAsociado__icontains="Financiamiento")
    elif request.user.groups.filter(name='Consultas_Propaganda').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="1_Nueva")
    elif request.user.groups.filter(name='Consultas_AdministracionE').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="1_Nueva")
    elif request.user.groups.filter(name='Consultas_Contabilidad').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="1_Nueva")
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
    ConsultasFormulario.objects.filter(ObjectID=int(data['datos']['ObjectID'])).update(Etapa=str(data['datos']['etapa']), Respuesta=str(data['datos']['respuesta']), Email=str(data['datos']['email']), Fecha_Respuesta=datetime.now())
    objeto = ConsultasFormulario.objects.filter(ObjectID=int(data['datos']['ObjectID']))
    WorkflowConsultas.objects.create(ObjectID=objeto[0].ObjectID, GlobalID=objeto[0].GlobalID, Usuario = request.user.username, NuevaEtapa = str(data['datos']['etapa']), FechaCambio = datetime.now())
    return JsonResponse([str(data['datos']['ObjectID']), 'Pasa'], safe=False)

def consultas_envio_respuestas(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like

    denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="3_Resuelta")
    context = {'todasdenuncias': denuncia_obj_3, 'user': request.user}
    return render(request,'Consultas/Consultas_Envio_Respuesta.html', context)

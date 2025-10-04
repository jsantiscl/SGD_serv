from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime, timedelta, time
from django.db.models import Count
from GestionRecursos.models import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.core.mail import send_mail
from ConsultasSCGYFE.models import *
from GestionDenuncias.models import Tokens
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from openpyxl import Workbook
import json, logging
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db import connection
from .models import ConsultasFormulario

def admin_consultas_total(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = ConsultasFormulario.objects.all()
    try:
        latest_token = Tokens.objects.latest('id')
        if latest_token and "&w=400" in latest_token.Token:
            latest_token.Token = latest_token.Token.replace("&w=400", "")
    except ObjectDoesNotExist:
        latest_token = None
    context = {'latest_token':latest_token, 'todasdenuncias': denuncia_obj_3}
    return render(request,'Consultas/Consultas.html', context)

def consultas_nuevas(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like

    if request.user.groups.filter(name='Consultas_Financiamiento').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="1_Nueva",
                                                            TemaAsociado__icontains="financiamiento")
    elif request.user.groups.filter(name='Consultas_Propaganda').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="1_Nueva",
                                                            TemaAsociado__icontains="propaganda")
    elif request.user.groups.filter(name='Consultas_DecProp').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="1_Nueva",
                                                            TemaAsociado__icontains="declaracionprop")
    elif request.user.groups.filter(name='Consultas_AdministracionE').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(
        Etapa__icontains="1_Nueva",
        TemaAsociado__icontains="administracion"
    ) | ConsultasFormulario.objects.filter(
        Etapa__icontains="1_Nueva",
        TemaAsociado__icontains="informe_de_gastos"
    )
    elif request.user.groups.filter(name='Consultas_Contabilidad').exists():
        denuncia_obj_3 = ConsultasFormulario.objects.filter(Etapa__icontains="1_Nueva",
                                                            TemaAsociado__icontains="contabilidad")
    try:
        latest_token = Tokens.objects.latest('id')
        if latest_token and "&w=400" in latest_token.Token:
            latest_token.Token = latest_token.Token.replace("&w=400", "")
    except ObjectDoesNotExist:
        latest_token = None
    context = {'latest_token':latest_token, 'todasdenuncias': denuncia_obj_3}
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

    try:
        latest_token = Tokens.objects.latest('id')
        if latest_token and "&w=400" in latest_token.Token:
            latest_token.Token = latest_token.Token.replace("&w=400", "")
    except ObjectDoesNotExist:
        latest_token = None
    context = {'latest_token':latest_token,'todasdenuncias': denuncia_obj_3, 'user': request.user}
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
    try:
        latest_token = Tokens.objects.latest('id')
        if latest_token and "&w=400" in latest_token.Token:
            latest_token.Token = latest_token.Token.replace("&w=400", "")
    except ObjectDoesNotExist:
        latest_token = None
    context = {'latest_token':latest_token,'todasdenuncias': denuncia_obj_3, 'user': request.user}
    return render(request,'Consultas/Consultas_Envio_Respuesta.html', context)


def consultas_respondidas(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like

    denuncia_obj_3 = ConsultasFormulario.objects.filter(Q(Etapa__icontains="2_Respuesta") | Q(Etapa__icontains="3_Resuelta")| Q(Etapa__icontains="4_Enviada"))
    try:
        latest_token = Tokens.objects.latest('id')
        if latest_token and "&w=400" in latest_token.Token:
            latest_token.Token = latest_token.Token.replace("&w=400", "")
    except ObjectDoesNotExist:
        latest_token = None
    context = {'latest_token':latest_token,'todasdenuncias': denuncia_obj_3, 'user': request.user}
    return render(request,'Consultas/Consultas_Respondidas.html', context)


def sandbox(request):

    context = {}
    return render(request,'Consultas/Sandbox.html', context)

logger = logging.getLogger(__name__)

@csrf_exempt
def carga_datos_consulta(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    data = request.POST.dict() if request.content_type != "application/json" else json.loads(request.body or "{}")
    tema = (data.get("TemaAsociado") or "").strip().lower()

    logger.info("nueva_respuesta DB=%s ENGINE=%s tema=%r keys=%s",
                connection.settings_dict.get("NAME"),
                connection.settings_dict.get("ENGINE"),
                tema,
                list(data.keys()))

    obj = ConsultasFormulario.objects.create(
        ObjectID=int(data.get("ObjectID")),
        GlobalID=data.get("GlobalID") or "SIN",
        NombreCompleto=data.get("NombreCompleto"),
        Rut=data.get("Rut"),
        TemaAsociado=tema,
        Pregunta=data.get("Pregunta"),
        Email=data.get("Email") or "SIN",
        FechaIngreso=timezone.now(),
        Etapa="1_Nueva",
        Adjunto=(data.get("Adjunto") or None),
    )

    logger.info("Insert OK tabla=%s id=%s", obj._meta.db_table, obj.pk)
    return JsonResponse({
        "ok": True,
        "id": obj.pk,
        "tabla": obj._meta.db_table,
        "db": connection.settings_dict.get("NAME"),
        "tema": tema,
    }, status=201)

def expcsv(request, lc):
    def remove_tzinfo(value):
        if isinstance(value, (datetime, time)):
            return value.replace(tzinfo=None)
        return value

    if lc == 'abecedconsultas':
        wb = Workbook()
        ws = wb.active

        # Opcionalmente, escribir los nombres de las columnas
        column_names = [field.name for field in ConsultasFormulario._meta.fields]
        ws.append(column_names)

        # Escribir los datos del modelo
        for obj in ConsultasFormulario.objects.all():
            row = [remove_tzinfo(getattr(obj, field.name)) for field in ConsultasFormulario._meta.fields]
            ws.append(row)

        # Configurar la respuesta HTTP
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Consultas.xlsx'

        # Guardar el libro de Excel en la respuesta
        wb.save(response)
        return response

    else:
        print("Error")
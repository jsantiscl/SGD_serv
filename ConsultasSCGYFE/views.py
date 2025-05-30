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


@csrf_exempt
def carga_datos_consulta(request):
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
        data = ConsultasFormulario(ObjectID=ObjectID,
                                   GlobalID=GlobalID,
                                   NombreCompleto=NombreCompleto,
                                   Rut=Rut,
                                   TemaAsociado=TemaAsociado,
                                   Pregunta=Pregunta,
                                   Email=Email,
                                   FechaIngreso=datetime.now(),
                                   Etapa='1_Nueva',
                                   Adjunto=Adjunto)

        # Guarda la instancia en la base de datos
        data.save()

        # Retorna una respuesta HTTP 200 si
        return HttpResponse('Datos guardados correctamente')
    else:
        # Retorna una respuesta HTTP 405 si se recibe una solicitud que no es POST
        return HttpResponse(status=405)

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
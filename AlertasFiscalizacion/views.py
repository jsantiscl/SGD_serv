from django.shortcuts import render

from django.shortcuts import redirect
from datetime import datetime
from django.db.models import Count
from AlertasFiscalizacion.models import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404
# Create your views here.

from django.conf import settings
from django.core.mail import send_mail
from GestionDenuncias.forms import *

# Create your views here.
def alertas(request):
    username_q = request.user.username
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    alertas = AlertasMeta.objects.filter(estado__icontains="1_Pendiente_Asignacion", usuario_actual__username=username_q)
    context = {'todasdenuncias': alertas}
    return render(request,'AlertasFiscalizacion/Alertas.html', context)

def alertas_asignadas(request):
    username_q = request.user.username
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    alertas = AlertasMeta.objects.filter(estado__icontains="2_Asignado_Abogado", usuario_actual__username=username_q)
    context = {'todasdenuncias': alertas}
    return render(request,'AlertasFiscalizacion/Alertas_asignadas.html', context)

def base_completa(request):
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    base = AnunciosMeta.objects.all()
    context = {'todasdenuncias': base}
    return render(request,'AlertasFiscalizacion/Base_Completa_Meta.html', context)

def detalle_base(request, nombre):
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    base = AnunciosMeta.objects.filter(nombre_homologado=nombre)
    context = {'todasdenuncias': base}
    return render(request,'AlertasFiscalizacion/detalle_anuncios.html', context)

def alarma_pasar_etapa(request):
    data = json.loads(request.body)


    AlertasMeta.objects.filter(id=str(data['datos']['id'])).update(estado=str(data['datos']['etapa']))
    AlertasMeta.objects.filter(id=str(data['datos']['id'])).update(usuario_actual=str(data['datos']['asignacion']))
    AlertasMeta.objects.filter(id=str(data['datos']['id'])).update(folio=str(data['datos']['folio']))
    AlertasMeta.objects.filter(id=str(data['datos']['id'])).update(link_adjuntos=str(data['datos']['carpeta']))
    AlertasMeta.objects.filter(id=str(data['datos']['id'])).update(obs_jefe=str(data['datos']['texto']))
    if (str(data['datos']['folio']) !=""):
        if str(data['datos']['asignacion']) == '2':
            abogado_id = 16749632
        if str(data['datos']['asignacion']) == '7':
            abogado_id = 16835392
        if str(data['datos']['asignacion']) == '8':
            abogado_id = 17995568
        if str(data['datos']['asignacion']) == '6':
            abogado_id = 16386974
        alerta = AlertasMeta.objects.filter(id=str(data['datos']['id']))
        Denuncias.objects.create(numero=str(data['datos']['folio']), fecha_ingreso_registro=datetime.now(),fecha_ingreso=datetime.now(),
                                 via_de_ingreso='LEVANTAMIENTO META',nombre_denunciante=alerta[0].tipo_alerta,nombre_denunciado=alerta[0].nombre_homologado,
                                 link_adjuntos = str(data['datos']['carpeta']), gestion = 'Pendiente', asignacion = 'Pendiente',
                                 estado_jefe='INGRESO', obs_ingreso=str(data['datos']['texto']),abogado_asistente_id=abogado_id)

    return JsonResponse([str(data['datos']['id']), 'Asignado'], safe=False)
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
    return JsonResponse([str(data['datos']['id']), 'Asignado'], safe=False)
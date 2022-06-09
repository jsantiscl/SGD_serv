from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from django.db.models import Count
from .models import Recursos
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404
# Create your views here.

def admin_recursos_total(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.all
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/GestionRecursos_Admin_Total.html', context)

def admin_recursos_asigna(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.all
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/GestionRecursos_Admin_Asignacion.html', context)

def ld_recursos_asigna(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="LD_asignacion_Lider")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/GestionRecursos_LD_Asignacion.html', context)



def asignar_recurso(request):
    data = json.loads(request.body)

    if data['datos']['asignacion'] == 'Pendiente':
         Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
    if data['datos']['asignacion'] != 'Pendiente':
        if data['datos']['asignacion'] != '11045585':
            Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='LD_asignacion_Lider')

        else:
            Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='XV_generacion_y_firma_reso_y_expediente')

    return JsonResponse([str(data['datos']['id']), 'Asignado'], safe=False)



def asignar_recurso_lider(request):
    data = json.loads(request.body)

    if data['datos']['asignacion'] == 'Pendiente':
         Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
    if data['datos']['asignacion'] != 'Pendiente':

        if data['datos']['asignacion'] == '19116154':
            Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='JC_asignacion_jefe_celula')
            Recursos.objects.filter(id=str(data['datos']['id'])).update(celula='c1')
        if data['datos']['asignacion'] == '12812146':
            Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='JC_asignacion_jefe_celula')
            Recursos.objects.filter(id=str(data['datos']['id'])).update(celula='c2')

        if data['datos']['asignacion'] == '18383521':
            Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='JC_asignacion_jefe_celula')
            Recursos.objects.filter(id=str(data['datos']['id'])).update(celula='c3')
        if data['datos']['asignacion'] == '18535049':
            Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='JC_asignacion_jefe_celula')
            Recursos.objects.filter(id=str(data['datos']['id'])).update(celula='c4')
        if data['datos']['asignacion'] == '15665508':
            Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='JC_asignacion_jefe_celula')
            Recursos.objects.filter(id=str(data['datos']['id'])).update(celula='ccac1')
        if data['datos']['asignacion'] == '16870114':
            Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='JC_asignacion_jefe_celula')
            Recursos.objects.filter(id=str(data['datos']['id'])).update(celula='ccac2')

    return JsonResponse([str(data['datos']['id']), 'Asignado'], safe=False)

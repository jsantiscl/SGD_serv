from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from django.db.models import Count
from .models import Recursos, UsersRecursos, Bitacora
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

def jc_recursos_asigna(request):
    username_q = request.user.username
    celula_actual = UsersRecursos.objects.filter(username__icontains=username_q)[0]
    auditores_celula = UsersRecursos.objects.filter(celula__icontains=celula_actual.celula, tipo__icontains="Auditor_jr")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="JC_asignacion_jefe_celula")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': auditores_celula}
    return render(request,'GestionRecursos/GestionRecursos_JC_Asignacion.html', context)


def au_informe_tecnico(request):
    username_q = request.user.username
    celula_actual = UsersRecursos.objects.filter(username__icontains=username_q)[0]
    auditores_celula = UsersRecursos.objects.filter(celula__iexact=celula_actual.celula, tipo__icontains="Jefe Celula")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="AU_realizacion_informe_tecnico")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': auditores_celula}
    return render(request,'GestionRecursos/GestionRecursos_AU_InformeTecnico.html', context)


####################################### ABAJO PROCESOS #######################################################

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
            Recursos.objects.filter(id=str(data['datos']['id'])).update(celula='ccac_1')
        if data['datos']['asignacion'] == '16870114':
            Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
            Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='JC_asignacion_jefe_celula')
            Recursos.objects.filter(id=str(data['datos']['id'])).update(celula='ccac_2')
        Usuario = UsersRecursos.objects.filter(rut=int(data['datos']['asignacion']))[0]
        Recurso_dato = Recursos.objects.filter(id=int(data['datos']['id']))[0]
        Bitacora.objects.create(username=Usuario, fecha_inicio=datetime.now(), id_recurso=Recurso_dato, etapa = 'JC_asignacion_jefe_celula' )

    return JsonResponse([str(data['datos']['id']), 'Asignado'], safe=False)



def asignar_recurso_jc(request):
    data = json.loads(request.body)
    if data['datos']['asignacion'] != 'Pendiente':
        Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
        Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='AU_realizacion_informe_tecnico')

        Usuario = UsersRecursos.objects.filter(rut=int(data['datos']['asignacion']))[0]
        Recurso_dato = Recursos.objects.filter(id=int(data['datos']['id']))[0]
        Bitacora.objects.create(username=Usuario, fecha_inicio=datetime.now(), id_recurso=Recurso_dato, etapa = 'AU_realizacion_informe_tecnico' )

    return JsonResponse([str(data['datos']['id']), 'Asignado'], safe=False)


def au_pasar_etapa(request):
    data = json.loads(request.body)
    if data['datos']['asignacion'] != 'Pendiente':
        Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
        Recursos.objects.filter(id=str(data['datos']['id'])).update(estado=str(data['datos']['etapa']))

        Usuario = UsersRecursos.objects.filter(rut=int(data['datos']['asignacion']))[0]
        Recurso_dato = Recursos.objects.filter(id=int(data['datos']['id']))[0]
        Bitacora.objects.create(username=Usuario, fecha_inicio=datetime.now(), id_recurso=Recurso_dato, etapa=str(data['datos']['etapa']))

    return JsonResponse([str(data['datos']['id']), 'Asignado'], safe=False)

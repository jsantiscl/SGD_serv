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

from django.conf import settings
from django.core.mail import send_mail



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

def jc_valida_informe_tecnico(request):
    username_q = request.user.username
    celula_actual = UsersRecursos.objects.filter(username__icontains=username_q)[0]
    abogados_celula = UsersRecursos.objects.filter(celula__iexact=celula_actual.celula, tipo__icontains="Abogado_C")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="JC_analisis_caso_jefe_celula")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_JC_Validacion_Informe_Tecnico.html', context)

def ab_elabora_propuesta(request):
    username_q = request.user.username
    celula_actual = UsersRecursos.objects.filter(username__icontains=username_q)[0]
    abogados_celula = UsersRecursos.objects.filter(celula__iexact=celula_actual.celula, tipo__icontains="Jefe Celula")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="AB_elaboracion_Propuesta")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_AB_ElaboracionPropuesta.html', context)

def reporte_vista(request):
    username_q = request.user.username
    celula_actual = UsersRecursos.objects.filter(username__icontains=username_q)[0]
    abogados_celula = UsersRecursos.objects.filter(celula__iexact=celula_actual.celula, tipo__icontains="Jefe Celula")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="AB_elaboracion_Propuesta")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_reporte.html', context)


def jc_valida_propuesta(request):
    username_q = request.user.username
    celula_actual = UsersRecursos.objects.filter(username__icontains=username_q)[0]
    if celula_actual.celula == 'c1' or celula_actual.celula == 'c2' or celula_actual.celula == 'c3' or celula_actual.celula == 'c4':
        abogados_celula = UsersRecursos.objects.filter(celula__iexact="ab_valida", tipo__icontains="ab_valida")
        #Aca en icontains pongo el filtro con el metodo icontains que es un like
        denuncia_obj_3 = Recursos.objects.filter(estado__icontains="JC_Validacion")
    else:
        abogados_celula = UsersRecursos.objects.filter(celula__iexact="ab_validaAc", tipo__icontains="ab_validaAc")
        #Aca en icontains pongo el filtro con el metodo icontains que es un like
        denuncia_obj_3 = Recursos.objects.filter(estado__icontains="JC_Validacion")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_JC_ValidaPropuesta.html', context)

def ab_valida_propuesta(request):
    username_q = request.user.username
    celula_actual = UsersRecursos.objects.filter(username__icontains=username_q)[0]

    if celula_actual.celula == 'c1' or celula_actual.celula == 'c2' or celula_actual.celula == 'c3' or celula_actual.celula == 'c4' or celula_actual.celula == 'ab_valida':
        abogados_celula = UsersRecursos.objects.filter(celula__iexact='NoDefinida', tipo__icontains="LiderC")
        #Aca en icontains pongo el filtro con el metodo icontains que es un like
        denuncia_obj_3 = Recursos.objects.filter(estado__icontains="ABVAL_revision_propuesta")
    else:
        abogados_celula = UsersRecursos.objects.filter(celula__iexact='NoDefinida', tipo__icontains="LiderAC")
        #Aca en icontains pongo el filtro con el metodo icontains que es un like
        denuncia_obj_3 = Recursos.objects.filter(estado__icontains="ABVAL_revision_propuesta")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_ABVAL_ValidacionPropuesta.html', context)

def formatosydocumentos(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    context = {}
    return render(request,'GestionRecursos/GestionRecursos_FormatosyDocumentos.html', context)

def ld_valida_propuesta(request):
    abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="JefeDivision")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="LD_en_validacion_lider")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_LD_ValidacionPropuesta.html', context)

def jd_valida_propuesta(request):
    abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Subdirector")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="JD_en_validacion_jd")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_JD_ValidacionPropuesta.html', context)

def sd_valida_propuesta(request):
    abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Doc")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="SD_en_validacion_sd")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_SD_ValidacionPropuesta.html', context)

def xv_genera_expediente(request):
    abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Rec")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="XV_generacion_y_firma_reso_y_expediente")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_XV_Bandeja1.html', context)

def xv_envia_tricel(request):
    abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Rec")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="XV_enviar_tricel")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_XV_Bandeja2.html', context)

def xv_monitoreo_sentencia(request):
    abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Rec")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="XV_monitoreo")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_XV_Bandeja3.html', context)

def gd_subir_a_firma(request):
    abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Doc")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="GD_Subir_sistema_datasoft")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_GD_SubiraFirma.html', context)

def gd_en_firma_director(request):
    abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Not")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="GD_en_firma_director")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_GD_en_Firma_Director.html', context)

def gd_en_notificacion(request):
    abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Doc")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="GD_en_Notificacion")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_GD_Notificacion.html', context)
def fin_revision_pagos(request):
    abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Doc")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="GD_en_Notificacion")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_FIN_Pagos.html', context)
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


def enviar_correo(request):
    data = json.loads(request.body)
    try:
        Usuario = UsersRecursos.objects.filter(rut=int(data['datos']['asignacion']))[0]
        User = UsersRecursos.objects.filter(username=Usuario.username)

        send_mail(
            'Asignacion Para Firma',
            'Estimado, Se le han asignado Recursos para subir a Firma, Favor ingresar a http://serv.jasb.cl Gracias',
            settings.EMAIL_HOST_USER,
            [str(User.email)],
            fail_silently=False
        )
        print("ok")
    except:
        print("error_envio")


    return JsonResponse([str(data['datos']['asignacion']), 'Asignado'], safe=False)

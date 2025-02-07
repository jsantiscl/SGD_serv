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
from GestionDenuncias.forms import *

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse



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
   #denuncia_obj_3 = Recursos.objects.filter(estado__icontains="LD_asignacion_Lider")
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="1_simpl_rep_asignacion_lider")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/GestionRecursos_LD_Asignacion.html', context)

def ab_recursos_asigna(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
   #denuncia_obj_3 = Recursos.objects.filter(estado__icontains="LD_asignacion_Lider")
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="4_simpl_rep_abogada_asignacion")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/GestionRecursos_AB_Asignacion.html', context)


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
    #celula_actual = UsersRecursos.objects.filter(username__icontains=username_q)[0]
    #auditores_celula = UsersRecursos.objects.filter(celula__iexact=celula_actual.celula, tipo__icontains="Jefe Celula")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    #denuncia_obj_3 = Recursos.objects.filter(estado__icontains="AU_realizacion_informe_tecnico")
    #context = {'todasdenuncias': denuncia_obj_3, 'auditores': auditores_celula}
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="2_simpl_rep_informe_tecnico")
    context = {'todasdenuncias': denuncia_obj_3}
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
    #celula_actual = UsersRecursos.objects.filter(username__icontains=username_q)[0]
    #abogados_celula = UsersRecursos.objects.filter(celula__iexact=celula_actual.celula, tipo__icontains="Jefe Celula")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="5_simpl_rep_abogados_propuesta")
    context = {'todasdenuncias': denuncia_obj_3}
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
    abogados_celula = UsersRecursos.objects.filter(tipo__icontains="ab_valida")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="JC_Validacion")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_JC_ValidaPropuesta.html', context)

def ab_valida_propuesta(request):
    #username_q = request.user.username
    #celula_actual = UsersRecursos.objects.filter(username__icontains=username_q)[0]
    #abogados_celula = UsersRecursos.objects.filter(celula__iexact='NoDefinida', tipo__icontains="LiderAC")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="6_simpl_rep_abogada_revision")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/GestionRecursos_ABVAL_ValidacionPropuesta.html', context)

def formatosydocumentos(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    context = {}
    return render(request,'GestionRecursos/GestionRecursos_FormatosyDocumentos.html', context)

def ld_valida_propuesta_ac(request):
    #abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="LiderC")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    #denuncia_obj_3 = Recursos.objects.filter(estado__icontains="LD_en_validacion_lider")
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="3_simpl_rep_informe_tecnico_revision_lider")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/GestionRecursos_LD_ValidacionPropuesta_ac.html', context)

def ld_valida_propuesta(request):
    #abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="JefeDivision")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    #denuncia_obj_3 = Recursos.objects.filter(estado__icontains="LD_en_validacion_lider")
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="3_simpl_rep_informe_tecnico_revision_lider")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/GestionRecursos_LD_ValidacionPropuesta.html', context)

def jd_valida_propuesta(request):
    #abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Subdirector")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="7_simpl_rep_revision_JD")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/GestionRecursos_JD_ValidacionPropuesta.html', context)

def sd_valida_propuesta(request):
    #abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Doc")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="8_simpl_rep_revision_SD")
    context = {'todasdenuncias': denuncia_obj_3}
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
    #abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Doc")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="10_simpl_rep_subida_pasarela")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/GestionRecursos_GD_SubiraFirma.html', context)

def gd_en_firma_director(request):
    abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Not")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="GD_en_firma_director")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_GD_en_Firma_Director.html', context)

def gd_en_notificacion(request):
    #abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Doc")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="11_simpl_rep_notificacion")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/GestionRecursos_GD_Notificacion.html', context)

def gd_subir_sge(request):
    abogados_celula = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="LiderAC")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="GD_subida_sge")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': abogados_celula}
    return render(request,'GestionRecursos/GestionRecursos_GD_SubirSGE.html', context)

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
        Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
        Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
        Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='2_simpl_rep_informe_tecnico')
        Recursos.objects.filter(id=str(data['datos']['id'])).update(celula='c1')

        Usuario = UsersRecursos.objects.filter(rut=int(data['datos']['asignacion']))[0]
        Recurso_dato = Recursos.objects.filter(id=int(data['datos']['id']))[0]
        Bitacora.objects.create(username=Usuario, fecha_inicio=datetime.now(), id_recurso=Recurso_dato, etapa = '2_simpl_rep_informe_tecnico' )

    return JsonResponse([str(data['datos']['id']), 'Asignado'], safe=False)

def ab_asignar_recurso_lider(request):
    data = json.loads(request.body)

    if data['datos']['asignacion'] == 'Pendiente':
         Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
    if data['datos']['asignacion'] != 'Pendiente':
        Recursos.objects.filter(id=str(data['datos']['id'])).update(prioridad=str(data['datos']['prioridad']))
        Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
        Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='5_simpl_rep_abogados_propuesta')
        Recursos.objects.filter(id=str(data['datos']['id'])).update(celula='c1')

        Usuario = UsersRecursos.objects.filter(rut=int(data['datos']['asignacion']))[0]
        Recurso_dato = Recursos.objects.filter(id=int(data['datos']['id']))[0]
        Bitacora.objects.create(username=Usuario, fecha_inicio=datetime.now(), id_recurso=Recurso_dato, etapa = '5_simpl_rep_abogados_propuesta' )

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
    if data['datos']['asignacion'] != 'Pendiente' and data['datos']['asignacion'] != '17311254':
        Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
        Recursos.objects.filter(id=str(data['datos']['id'])).update(estado=str(data['datos']['etapa']))
        Usuario = UsersRecursos.objects.filter(rut=int(data['datos']['asignacion']))[0]
        Recurso_dato = Recursos.objects.filter(id=int(data['datos']['id']))[0]
        Bitacora.objects.create(username=Usuario, fecha_inicio=datetime.now(), id_recurso=Recurso_dato, etapa=str(data['datos']['etapa']))
    if data['datos']['asignacion'] == '17311254':
        Recursos.objects.filter(id=str(data['datos']['id'])).update(estado='fin_proceso_finalizado')
        Recursos.objects.filter(id=str(data['datos']['id'])).update(usuario_actual_id=str(data['datos']['asignacion']))
        Usuario = UsersRecursos.objects.filter(rut=int(data['datos']['asignacion']))[0]
        Recurso_dato = Recursos.objects.filter(id=int(data['datos']['id']))[0]
        Bitacora.objects.create(username=Usuario, fecha_inicio=datetime.now(), id_recurso=Recurso_dato, etapa='fin_proceso_finalizado')

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


### Plebiscito

def total_solicitudes(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = InscripcionesPlebiscito.objects.filter(estado='ENVIADO')
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/Plebiscito_Total_Inscritos.html', context)

def asigna_admin_inscripciones(request):
    auditores = UsersRecursos.objects.filter(celula__iexact="NoDefinida", tipo__icontains="Gest_Doc")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Recursos.objects.filter(estado__icontains="GD_en_Notificacion")
    context = {'todasdenuncias': denuncia_obj_3, 'auditores': auditores}

    return render(request,'GestionRecursos/Plebiscito_Total_Inscritos.html', context)

def revision_inscripciones(request):
    username_q = request.user.username
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = InscripcionesPlebiscito.objects.filter(etapa_revision='REVISION_AUDITOR', estado='ENVIADO', usuario_actual__username=username_q)
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request,'GestionRecursos/Plebiscito_Revision_Casos.html', context)

def revisa_particular_pleb(request, id_pleb):
    instance = get_object_or_404(InscripcionesPlebiscito, id=id_pleb)
    denuncia_obj_4 = InscripcionesPlebiscito.objects.filter(id=id_pleb)
    adjuntos_pleb = AdjuntosInscripciones.objects.filter(id_registro=id_pleb)
    rl_pleb = RepresentanteLegal.objects.filter(id_org=id_pleb)
    form = DetallesInscripcion(request.POST or None, instance=instance)
    form2 = RevisaCasos(request.POST or None)
    context = {'todasdenuncias': denuncia_obj_4, 'form': form, 'form2': form2, 'adjuntos_pleb': adjuntos_pleb, 'rl_pleb': rl_pleb}
    return render(request,'GestionRecursos/Plebiscito_Revision_Casos_Particular.html', context)


def pleb_pasar_etapa(request):
    data = json.loads(request.body)
    InscripcionesPlebiscito.objects.filter(id=str(data['datos']['id'])).update(etapa_revision='VALIDACION_ADMIN')
    RevisionesInscripciones.objects.create(id=int(data['datos']['id']), revisor=str(data['datos']['revisor']), valida_adjunto=str(data['datos']['valida_adjunto']), valida_sin_fines_de_lucro=str(data['datos']['valida_sin_fines_de_lucro']),propuesta=str(data['datos']['propuesta']), comentarios_revisor =str(data['datos']['comentarios_revisor']))
    return JsonResponse([str(data['datos']['id']), 'Asignado'], safe=False)


@csrf_exempt
def carga_datos(request):
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
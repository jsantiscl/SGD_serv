from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from django.db.models import Sum, Count
from .models import Denuncias, Adjuntos, Abogados
from .forms import DenunciasForm, ResumeUpload, UpdateDetailsForm, ActivaDenuncia, DetallesDenuncia, DesactivaDenuncia, CompruebaDenuncia
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import xlrd
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404

def denuncias_ingreso(request):
    if request.method == 'POST':
        form = DenunciasForm(request.POST, request.FILES)
        files = request.FILES.getlist('adjunto_denuncia')
        if form.is_valid():
            instancia = form.save(commit=False)
            form.save()
            for f in files:
                file_instance = Adjuntos(id_denuncia=instancia, archivos=f, tipo='adjunto_denuncia')
                file_instance.save()
            return redirect('denuncias_ingreso')
    else:
        form = DenunciasForm()

    lista_abogados = Abogados.objects.filter(habilitado=True)


    context = {'form': form, 'lista_abogados': lista_abogados}
    return render(request, 'GestionDenuncias/admin_ingreso_individual.html', context)


def denuncias_ingreso_mass(request):
    message = ''
    if request.method == 'POST':
        form = UpdateDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            # import your django model here like from django.appname.models import model_name
            excel_file = request.FILES['excel_file']
            import os
            import tempfile
            import xlrd
            fd, path = tempfile.mkstemp()  # mkstemp returns a tuple: an integer (index) called file descriptor used by OS to refer to a file and its path
            try:
                with os.fdopen(fd, 'wb') as tmp:
                    tmp.write(excel_file.read())
                book = xlrd.open_workbook(path)
                sheet = book.sheet_by_index(0)
                for rx in range(1, sheet.nrows):
                    obj = Denuncias(
                        numero=sheet.cell_value(rowx=rx, colx=0),
                        link_adjuntos=sheet.cell_value(rowx=rx, colx=1),
                        fecha_ingreso=sheet.cell_value(rowx=rx, colx=2),
                        via_de_ingreso=sheet.cell_value(rowx=rx, colx=3),
                        nombre_denunciante=sheet.cell_value(rowx=rx, colx=4),
                        nombre_denunciado=sheet.cell_value(rowx=rx, colx=5),
                        obs_ingreso=sheet.cell_value(rowx=rx, colx=6),
                        abogado_asistente_id=sheet.cell_value(rowx=rx, colx=7)
                    )
                    obj.save()
            finally:
                os.remove(path)
        else:
            message = 'Invalid Entries'
    else:
        form = UpdateDetailsForm()

    lista_abogados = Abogados.objects.filter(habilitado=True)

    context = {'form': form, 'message': message, 'lista_abogados': lista_abogados}
    return render(request,'GestionDenuncias/ingreso_masivo.html', context)

    #return render(request, 'GestionDenuncias/ingreso_masivo.html', context)


def jefe_inicio(request):
    return render(request, 'GestionDenuncias/jefe_inicio.html')

def jefe_pendientes(request):
    denuncia_obj = Denuncias.objects.filter(estado_jefe__icontains="INGRESO")
    adjuntos_obj = Adjuntos.objects.filter(tipo__icontains="adjunto_denuncia")
    if request.method == 'POST':

        for denuncia in denuncia_obj:
            i = denuncia.id
            if request.POST.get(str(i+100000000)) != "Pendiente":
                Denuncias.objects.filter(id=str(i)).update(materia=request.POST.get(str(i+100000000)))
                Denuncias.objects.filter(id=str(i)).update(infraccion_denunciada=request.POST.get(str(i + 200000000)))
                Denuncias.objects.filter(id=str(i)).update(estado_jefe="CLASIFICADO")
        return redirect("jefe_pendientes_i")

    #Aca en icontains pongo el filtro con el metodo icontains que es un like

    context = {'todasdenuncias': denuncia_obj, 'todosadjuntos': adjuntos_obj}
    return render(request, 'GestionDenuncias/jefe_bandeja_pendientes.html', context)

def jefe_pendientes_instruccion(request):
    denuncia_obj_2 = Denuncias.objects.filter(estado_jefe__icontains="CLASIFICADO")
    adjuntos_obj = Adjuntos.objects.filter(tipo__icontains="adjunto_denuncia")

    if request.method == 'POST':

        for denuncia in denuncia_obj_2:
            i = denuncia.id
            if request.POST.get(str(i + 300000000)) != "Pendiente":
                if request.POST.get(str(i + 400000000)) != "Pendiente":
                    Denuncias.objects.filter(id=str(i)).update(gestion=request.POST.get(str(i+300000000)))
                    Denuncias.objects.filter(id=str(i)).update(asignacion=request.POST.get(str(i+400000000)))
                    if request.POST.get(str(i+500000000)) == 'True':
                        Denuncias.objects.filter(id=str(i)).update(diligencia_sad=True)
                    if request.POST.get(str(i+600000000)) == 'True':
                        Denuncias.objects.filter(id=str(i)).update(diligencia_req_inf=True)
                    if request.POST.get(str(i+700000000)) == 'True':
                        Denuncias.objects.filter(id=str(i)).update(diligencia_citacion=True)
                    if request.POST.get(str(i+800000000)) == 'True':
                        Denuncias.objects.filter(id=str(i)).update(diligencia_insp_terreno=True)
                    if request.POST.get(str(i+900000000)) == 'True':
                        Denuncias.objects.filter(id=str(i)).update(diligencia_insp_remota=True)
                    if request.POST.get(str(i+1000000000)) == 'True':
                        Denuncias.objects.filter(id=str(i)).update(diligencia_subsanacion=True)
                    if request.POST.get(str(i+1100000000)) == 'True':
                        Denuncias.objects.filter(id=str(i)).update(diligencia_orden_retiro=True)
                    if request.POST.get(str(i+1200000000)) == 'True':
                        Denuncias.objects.filter(id=str(i)).update(diligencia_otra=True)

                    Denuncias.objects.filter(id=str(i)).update(estado_jefe="ENVIADO_JEFE")
                    Denuncias.objects.filter(id=str(i)).update(plazo_investigacion=request.POST.get(str(i+1300000000)))
                    Denuncias.objects.filter(id=str(i)).update(abogado_asistente=request.POST.get(str(i+1400000000)))

        return redirect("jefe_pendientes_i")

    #Aca en icontains pongo el filtro con el metodo icontains que es un like

    context = {'todasdenuncias': denuncia_obj_2, 'todosadjuntos': adjuntos_obj}
    return render(request, 'GestionDenuncias/jefe_bandeja_pendientes_instruccion.html', context)



def jefe_enviados(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Denuncias.objects.filter(estado_jefe__icontains="ENVIADO_JEFE")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request, 'GestionDenuncias/jefe_bandeja_enviados.html', context)


def abogado_inicio(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Denuncias.objects.filter(estado_jefe__icontains="ENVIADO_JEFE")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request, 'GestionDenuncias/abogado_inicio.html', context)


def abogado_gestiones(request):
    adjuntos_obj = Adjuntos.objects.filter(tipo__icontains="adjunto_denuncia")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Denuncias.objects.filter(estado_jefe__icontains="ENVIADO_JEFE")
    context = {'todasdenuncias': denuncia_obj_3, 'todosadjuntos': adjuntos_obj}
    return render(request, 'GestionDenuncias/abogado_gestiones.html', context)

def abogado_evaluacion(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Denuncias.objects.filter(estado_jefe__icontains="INGRESO")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request, 'GestionDenuncias/abogado_evaluacion.html', context)

def abogado_rechazos(request):
    denuncia_obj_3 = Denuncias.objects.filter(estado_jefe__icontains="DEVUELTO_JEFE")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request, 'GestionDenuncias/abogado_rechazos.html', context)


def jefe_evaluacion_act(request):
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Denuncias.objects.filter(estado_jefe__icontains="ACTIVADA_COMPROBADA_ABOGADO")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request, 'GestionDenuncias/jefe_evaluacion_act.html', context)

def jefe_evaluacion_desact(request):
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Denuncias.objects.filter(estado_jefe__icontains="DESACTIVADO_ENVIADO_ABOGADO")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request, 'GestionDenuncias/jefe_evaluacion_desact.html', context)

def validacion_masiva(request):
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Denuncias.objects.filter(estado_jefe__icontains="DESACTIVADO_ENVIADO_ABOGADO")
    codigos = Denuncias.objects.values('codigo_desactivacion') \
  .annotate(cantidad=Count('numero')) \
        .filter(estado_jefe__icontains='DESACTIVADO_ENVIADO_ABOGADO')

    context = {'todasdenuncias': denuncia_obj_3, 'codigos': codigos}
    return render(request, 'GestionDenuncias/jefe_validacion_masiva.html', context)


def abogado_comprobacion(request):
    adjuntos_obj = Adjuntos.objects.filter(tipo__icontains="adjunto_denuncia")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Denuncias.objects.filter(estado_jefe__icontains="INGRESO")
    context = {'todasdenuncias': denuncia_obj_3, 'todosadjuntos': adjuntos_obj}
    return render(request, 'GestionDenuncias/abogado_comprobacion.html', context)

def gestion_denuncia_comp(request, id_denuncia):
    instance = get_object_or_404(Denuncias, id=id_denuncia)
    denuncia_obj_4 = Denuncias.objects.filter(id=id_denuncia)
    form = CompruebaDenuncia(request.POST or None, instance=instance)
    form2 = DetallesDenuncia(request.POST or None, instance=instance)

    context = {'todasdenuncias': denuncia_obj_4, 'form': form, 'form2': form2}

    if request.method == 'POST':

            if request.POST.get(str("guardac")) == 'SI':
                Denuncias.objects.filter(id=str(id_denuncia)).update(estado_jefe="ACTIVADA_COMPROBADA_ABOGADO")
                Denuncias.objects.filter(id=str(id_denuncia)).update(fecha_comprobacion_abogado=datetime.now())
                Denuncias.objects.filter(id=str(id_denuncia)).update(resultado_comprobacion=request.POST.get(str("resultado_comprobacion")))
                Denuncias.objects.filter(id=str(id_denuncia)).update(obs_abogado=request.POST.get(str("obs_abogado")))
                return redirect("abogado_comprobacion")
            if request.POST.get(str("guardac")) == 'NO':
                Denuncias.objects.filter(id=str(id_denuncia)).update(resultado_comprobacion=request.POST.get(str("resultado_comprobacion")))
                Denuncias.objects.filter(id=str(id_denuncia)).update(obs_abogado=request.POST.get(str("obs_abogado")))
                return redirect("abogado_comprobacion")

    return render(request, 'GestionDenuncias/abogado_gestionar_denuncia_comprob.html', context)

############## TENGO QUE AGREGAR LA VIEW abogado_gestion_denuncia ver como hacer para tener los path el id

def abogado_gestion_denuncia(request, id_denuncia):

    denuncia_obj_4 = Denuncias.objects.filter(id=id_denuncia)
    adjuntos_obj_1 = Adjuntos.objects.filter(tipo__icontains="SAD_SOLICITUD", id_denuncia_id=id_denuncia)
    adjuntos_obj_2 = Adjuntos.objects.filter(tipo__icontains="REQ_INF_SOLICITUD_", id_denuncia_id=id_denuncia)
    adjuntos_obj_3 = Adjuntos.objects.filter(tipo__icontains="CIT_SOLICITUD_", id_denuncia_id=id_denuncia)
    adjuntos_obj_4 = Adjuntos.objects.filter(tipo__icontains="INSP_TERR_SOLICITUD_", id_denuncia_id=id_denuncia)
    adjuntos_obj_5 = Adjuntos.objects.filter(tipo__icontains="INSP_REM_SOLICITUD_", id_denuncia_id=id_denuncia)
    adjuntos_obj_6 = Adjuntos.objects.filter(tipo__icontains="REQ_SUB_SOLICITUD_", id_denuncia_id=id_denuncia)
    adjuntos_obj_7 = Adjuntos.objects.filter(tipo__icontains="ORD_RET_SOLICITUD_", id_denuncia_id=id_denuncia)

    context = {'todasdenuncias': denuncia_obj_4, 'adjuntos_obj_1': adjuntos_obj_1,  'adjuntos_obj_2': adjuntos_obj_2, 'adjuntos_obj_3': adjuntos_obj_3,  'adjuntos_obj_4': adjuntos_obj_4, 'adjuntos_obj_5': adjuntos_obj_5,  'adjuntos_obj_6': adjuntos_obj_6, 'adjuntos_obj_7': adjuntos_obj_7}

    if request.method == 'POST':
        for denuncia in denuncia_obj_4:
            i = denuncia.id
            if request.POST.get(str(i+1500000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_sol_sad=request.POST.get(str(i+1500000000)))
            if request.POST.get(str(i + 1500000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_sol_sad= None)

            if request.POST.get(str(i+1600000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_sol_req=request.POST.get(str(i+1600000000)))
            if request.POST.get(str(i + 1600000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_sol_req=None)

            if request.POST.get(str(i+1700000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_citacion=request.POST.get(str(i+1700000000)))
            if request.POST.get(str(i+1700000000)) =="":
                Denuncias.objects.filter(id=str(i)).update(fecha_citacion=None)

            if request.POST.get(str(i+1800000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_inspeccion_terr=request.POST.get(str(i+1800000000)))
            if request.POST.get(str(i+1800000000)) =="":
                Denuncias.objects.filter(id=str(i)).update(fecha_inspeccion_terr=None)

            if request.POST.get(str(i+1900000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(unidad_fiscalizada_terr=request.POST.get(str(i+1900000000)))
            if request.POST.get(str(i + 1900000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(unidad_fiscalizada_terr=None)

            if request.POST.get(str(i+2000000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_inspeccion_rem=request.POST.get(str(i+2000000000)))
            if request.POST.get(str(i + 2000000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_inspeccion_rem=None)

            if request.POST.get(str(i+2100000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(unidad_fiscalizada_rem=request.POST.get(str(i+2100000000)))
            if request.POST.get(str(i + 2100000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(unidad_fiscalizada_rem=None)

            if request.POST.get(str(i+2200000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_inspeccion_sub=request.POST.get(str(i+2200000000)))
            if request.POST.get(str(i + 2200000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_inspeccion_sub=None)

            if request.POST.get(str(i+2300000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(unidad_fiscalizada_sub=request.POST.get(str(i+2300000000)))
            if request.POST.get(str(i + 2300000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(unidad_fiscalizada_sub=None)

            if request.POST.get(str(i+2400000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_requer=request.POST.get(str(i+2400000000)))
            if request.POST.get(str(i + 2400000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_requer=None)

            if request.POST.get(str(i+2500000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(municipalidad=request.POST.get(str(i+2500000000)))
            if request.POST.get(str(i+2500000000)) =="":
                Denuncias.objects.filter(id=str(i)).update(municipalidad=None)

            try:
                if request.FILES.getlist(str(i + 3900000000)) != "":
                    files = request.FILES.getlist(str(i + 3900000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='SAD_SOLICITUD')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_sol_sad=True)
            except:
                print("no")

            try:
                if request.FILES.getlist(str(i + 4000000000)) != "":
                    files = request.FILES.getlist(str(i + 4000000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='REQ_INF_SOLICITUD_')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_sol_req_inf=True)
            except:
                print("no")

            try:
                if request.FILES.getlist(str(i + 4100000000)) != "":
                    files = request.FILES.getlist(str(i + 4100000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='CIT_SOLICITUD_')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_sol_cit=True)
            except:
                print("no")
            try:
                if request.FILES.getlist(str(i + 4200000000)) != "":
                    files = request.FILES.getlist(str(i + 4200000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='INSP_TERR_SOLICITUD_')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_sol_ins_terr=True)
            except:
                print("no")

            try:
                if request.FILES.getlist(str(i + 4300000000)) != "":
                    files = request.FILES.getlist(str(i + 4300000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='INSP_REM_SOLICITUD_')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_sol_ins_rem=True)
            except:
                print("no")

            try:
                if request.FILES.getlist(str(i + 4400000000)) != "":
                    files = request.FILES.getlist(str(i + 4400000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='REQ_SUB_SOLICITUD_')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_sol_req_sub=True)
            except:
                print("no")

            try:
                if request.FILES.getlist(str(i + 4500000000)) != "":
                    files = request.FILES.getlist(str(i + 4500000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='ORD_RET_SOLICITUD_')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_sol_ord_ret=True)
            except:
                print("no")

            if request.POST.get(str("button_enviar")):
                Denuncias.objects.filter(id=str(i)).update(estado_jefe="GEST_INGRESO_ABOGADO_REALIZADA")
                return redirect("abogado_gestiones")
            if request.POST.get(str("button_guardar")):
                return redirect("abogado_gestiones")

    return render(request, 'GestionDenuncias/abogado_gestionar_denuncia.html', context)




def abogado_gestion_denuncia_ac(request, id_denuncia):

    instance = get_object_or_404(Denuncias, id=id_denuncia)
    denuncia_obj_4 = Denuncias.objects.filter(id=id_denuncia)
    form = ActivaDenuncia(request.POST or None, instance=instance)
    form2 = DetallesDenuncia(request.POST or None, instance=instance)

    context = {'todasdenuncias': denuncia_obj_4, 'form': form, 'form2': form2}

    if request.method == 'POST':

            if form.is_valid():
                form.save()
            if request.POST.get(str("guarda")) == 'SI':
                Denuncias.objects.filter(id=str(id_denuncia)).update(estado_jefe="GEST_INGRESO_ABOGADO_REALIZADA")
                Denuncias.objects.filter(id=str(id_denuncia)).update(fecha_evaluacion_abogado=datetime.now())
                return redirect("abogado_evaluacion")
            if request.POST.get(str("guarda")) == 'NO':
                return redirect("abogado_evaluacion")
    return render(request, 'GestionDenuncias/abogado_gestionar_denuncia_activar.html', context)

def abogado_gestion_denuncia_desac(request, id_denuncia):

    instance = get_object_or_404(Denuncias, id=id_denuncia)
    denuncia_obj_4 = Denuncias.objects.filter(id=id_denuncia)
    form = DesactivaDenuncia(request.POST or None, instance=instance)
    form2 = DetallesDenuncia(request.POST or None, instance=instance)
    Denuncias.objects.filter(id=str(id_denuncia)).update(guarda="NO")

    context = {'todasdenuncias': denuncia_obj_4, 'form': form, 'form2': form2}

    if request.method == 'POST':

            if form.is_valid():
                form.save()
            if request.POST.get(str("guarda")) == 'SI':
                Denuncias.objects.filter(id=str(id_denuncia)).update(estado_jefe="DESACTIVADO_ENVIADO_ABOGADO")
                Denuncias.objects.filter(id=str(id_denuncia)).update(fecha_evaluacion_abogado=datetime.now())
                return redirect("abogado_evaluacion")
            if request.POST.get(str("guarda")) == 'NO':
                return redirect("abogado_evaluacion")

    return render(request, 'GestionDenuncias/abogado_gestionar_denuncia_desactivar.html', context)

def abogado_resultados(request):
    adjuntos_obj = Adjuntos.objects.filter(tipo__icontains="adjunto_denuncia")
    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_5 = Denuncias.objects.filter(estado_jefe__icontains="GEST_INGRESO_ABOGADO_REALIZADA")
    context = {'todasdenuncias': denuncia_obj_5, 'todosadjuntos': adjuntos_obj}
    return render(request, 'GestionDenuncias/abogado_resultados.html', context)


def abogado_resultado_denuncia(request, id_denuncia):

    denuncia_obj_6 = Denuncias.objects.filter(id=id_denuncia)
    adjuntos_obj_1 = Adjuntos.objects.filter(tipo__icontains="SAD_SOLICITUD", id_denuncia_id=id_denuncia)
    adjuntos_obj_2 = Adjuntos.objects.filter(tipo__icontains="REQ_INF_SOLICITUD_", id_denuncia_id=id_denuncia)
    adjuntos_obj_3 = Adjuntos.objects.filter(tipo__icontains="CIT_SOLICITUD_", id_denuncia_id=id_denuncia)
    adjuntos_obj_4 = Adjuntos.objects.filter(tipo__icontains="INSP_TERR_SOLICITUD_", id_denuncia_id=id_denuncia)
    adjuntos_obj_5 = Adjuntos.objects.filter(tipo__icontains="INSP_REM_SOLICITUD_", id_denuncia_id=id_denuncia)
    adjuntos_obj_6 = Adjuntos.objects.filter(tipo__icontains="REQ_SUB_SOLICITUD_", id_denuncia_id=id_denuncia)
    adjuntos_obj_7 = Adjuntos.objects.filter(tipo__icontains="ORD_RET_SOLICITUD_", id_denuncia_id=id_denuncia)

    adjuntos_obj_8 = Adjuntos.objects.filter(tipo__icontains="SAD_RESPUESTA", id_denuncia_id=id_denuncia)
    adjuntos_obj_9 = Adjuntos.objects.filter(tipo__icontains="REQ_INF_RESPUESTA", id_denuncia_id=id_denuncia)
    adjuntos_obj_10 = Adjuntos.objects.filter(tipo__icontains="CIT_RESPUESTA", id_denuncia_id=id_denuncia)
    adjuntos_obj_11 = Adjuntos.objects.filter(tipo__icontains="INSP_TERR_RESPUESTA", id_denuncia_id=id_denuncia)
    adjuntos_obj_12 = Adjuntos.objects.filter(tipo__icontains="INSP_REM_RESPUESTA", id_denuncia_id=id_denuncia)
    adjuntos_obj_13 = Adjuntos.objects.filter(tipo__icontains="REQ_SUB_RESPUESTA", id_denuncia_id=id_denuncia)
    adjuntos_obj_14 = Adjuntos.objects.filter(tipo__icontains="ORD_RET_RESPUESTA", id_denuncia_id=id_denuncia)
    adjuntos_obj_15 = Adjuntos.objects.filter(tipo__icontains="INFORME", id_denuncia_id=id_denuncia)

    context = {'todasdenuncias': denuncia_obj_6, 'adjuntos_obj_1': adjuntos_obj_1,  'adjuntos_obj_2': adjuntos_obj_2, 'adjuntos_obj_3': adjuntos_obj_3,  'adjuntos_obj_4': adjuntos_obj_4, 'adjuntos_obj_5': adjuntos_obj_5,  'adjuntos_obj_6': adjuntos_obj_6, 'adjuntos_obj_7': adjuntos_obj_7, 'adjuntos_obj_8': adjuntos_obj_8, 'adjuntos_obj_9': adjuntos_obj_9, 'adjuntos_obj_10': adjuntos_obj_10, 'adjuntos_obj_11': adjuntos_obj_11, 'adjuntos_obj_12': adjuntos_obj_12, 'adjuntos_obj_13': adjuntos_obj_13, 'adjuntos_obj_14': adjuntos_obj_14, 'adjuntos_obj_15': adjuntos_obj_15}

    if request.method == 'POST':
        for denuncia in denuncia_obj_6:
            i = denuncia.id
            if request.POST.get(str(i+9900000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_res_sad=request.POST.get(str(i+9900000000)))
            if request.POST.get(str(i + 9900000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_res_sad= None)

            if request.POST.get(str(i+2600000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_sad=request.POST.get(str(i+2600000000)))
            if request.POST.get(str(i + 2600000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_sad= None)

            if request.POST.get(str(i+2700000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_res_req=request.POST.get(str(i+2700000000)))
            if request.POST.get(str(i + 2700000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_res_req= None)

            if request.POST.get(str(i+2800000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_req=request.POST.get(str(i+2800000000)))
            if request.POST.get(str(i + 2800000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_req= None)

            if request.POST.get(str(i+2900000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_comparecencia=request.POST.get(str(i+2900000000)))
            if request.POST.get(str(i + 2900000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_comparecencia= None)

            if request.POST.get(str(i+3000000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_cit=request.POST.get(str(i+3000000000)))
            if request.POST.get(str(i + 3000000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_cit= None)

            if request.POST.get(str(i+3100000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_terr=request.POST.get(str(i+3100000000)))
            if request.POST.get(str(i+3100000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_terr= None)

            if request.POST.get(str(i+3200000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_rem=request.POST.get(str(i+3200000000)))
            if request.POST.get(str(i+3200000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_rem= None)

            if request.POST.get(str(i+3300000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_sub=request.POST.get(str(i+3300000000)))
            if request.POST.get(str(i+3300000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_sub= None)

            if request.POST.get(str(i+3400000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_orden_ret=request.POST.get(str(i+3400000000)))
            if request.POST.get(str(i+3400000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_orden_ret= None)

            if request.POST.get(str(i+3500000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_abogado=request.POST.get(str(i+3500000000)))
            if request.POST.get(str(i + 3500000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_abogado= None)

            if request.POST.get(str(i+3600000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(motivo_abogado=request.POST.get(str(i+3600000000)))
            if request.POST.get(str(i+3600000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(motivo_abogado= None)

            try:
                if request.FILES.getlist(str(i + 4600000000)) != "":
                    files = request.FILES.getlist(str(i + 4600000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='SAD_RESPUESTA')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_res_sad=True)
            except:
                print("no")

            try:
                if request.FILES.getlist(str(i + 4700000000)) != "":
                    files = request.FILES.getlist(str(i + 4700000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='REQ_INF_RESPUESTA')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_res_req_inf=True)
            except:
                print("no")

            try:
                if request.FILES.getlist(str(i + 4800000000)) != "":
                    files = request.FILES.getlist(str(i + 4800000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='CIT_RESPUESTA')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_res_cit=True)
            except:
                print("no")

            try:
                if request.FILES.getlist(str(i + 4900000000)) != "":
                    files = request.FILES.getlist(str(i + 4900000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='INSP_TERR_RESPUESTA')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_res_ins_terr=True)
            except:
                print("no")

            try:
                if request.FILES.getlist(str(i + 5000000000)) != "":
                    files = request.FILES.getlist(str(i + 5000000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='INSP_REM_RESPUESTA')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_res_ins_rem=True)
            except:
                print("no")

            try:
                if request.FILES.getlist(str(i + 5100000000)) != "":
                    files = request.FILES.getlist(str(i + 5100000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='REQ_SUB_RESPUESTA')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_res_req_sub=True)
            except:
                print("no")

            try:
                if request.FILES.getlist(str(i + 5200000000)) != "":
                    files = request.FILES.getlist(str(i + 5200000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='ORD_RET_RESPUESTA')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_res_ord_ret=True)
            except:
                print("no")


            try:
                if request.FILES.getlist(str(i + 5300000000)) != "":
                    files = request.FILES.getlist(str(i + 5300000000))
                    for f in files:
                        file_instance = Adjuntos(id_denuncia=denuncia, archivos=f, tipo='INFORME')
                        file_instance.save()
                        Denuncias.objects.filter(id=str(i)).update(tiene_adjunto_informe=True)
            except:
                print("no")


            if request.POST.get(str("button_enviar")):
                Denuncias.objects.filter(id=str(i)).update(estado_jefe="RESULTADO_ABOGADO_INGRESADO")
                return redirect("abogado_resultados")
            if request.POST.get(str("button_guardar")):
                return redirect("abogado_resultados")

    return render(request, 'GestionDenuncias/abogado_resultado_denuncia.html', context)


def abogado_enviados(request):
        # Aca en icontains pongo el filtro con el metodo icontains que es un like
        denuncia_obj_3 = Denuncias.objects.exclude(estado_jefe__icontains="INGRESO").exclude(estado_jefe__icontains="GEST_INGRESO_ABOGADO_REALIZADA")
        context = {'todasdenuncias': denuncia_obj_3}
        return render(request, 'GestionDenuncias/abogado_enviados.html', context)

######## ME FALTA HACER QUE PUEDA VER LA RESPUESTA DEL HUGO; Q PASE AL HUGO Y Q PUEDA CORREGIR CUANDO LO DEVUELVA

####### DESPUES ME FALTA HACER Q PUEDA RECIBIR ADJUNTOS; ALFRESCO U OTRO

def jefe_validacion(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_7 = Denuncias.objects.filter(estado_jefe__icontains="RESULTADO_ABOGADO")
    adjuntos_obj_15 = Adjuntos.objects.filter(tipo__icontains="INFORME")
    context = {'todasdenuncias': denuncia_obj_7, 'adjuntos_obj_15': adjuntos_obj_15}

    if request.method == 'POST':
        for denuncia in denuncia_obj_7:
            i = denuncia.id
            if request.POST.get(str(i+3700000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(estado_jefe=request.POST.get(str(i+3700000000)))
            if request.POST.get(str(i+3800000000)) != "":
                Denuncias.objects.filter(id=str(i)).update(obs_jefe=request.POST.get(str(i+3800000000)))
            return redirect("jefe_validacion")

    return render(request, 'GestionDenuncias/jefe_bandeja_validacion.html', context)

def abogado_rechazo_denuncia(request, id_denuncia):


    denuncia_obj_6 = Denuncias.objects.filter(id=id_denuncia)
    context = {'todasdenuncias': denuncia_obj_6}

    if request.method == 'POST':
        for denuncia in denuncia_obj_6:
            i = denuncia.id
            if request.POST.get(str(i + 1500000000)) != "":
                Denuncias.objects.filter(id=str(i)).update(fecha_sol_sad=request.POST.get(str(i + 1500000000)))
            if request.POST.get(str(i + 1500000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_sol_sad=None)

            if request.POST.get(str(i + 1600000000)) != "":
                Denuncias.objects.filter(id=str(i)).update(fecha_sol_req=request.POST.get(str(i + 1600000000)))
            if request.POST.get(str(i + 1600000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_sol_req=None)

            if request.POST.get(str(i + 1700000000)) != "":
                Denuncias.objects.filter(id=str(i)).update(fecha_citacion=request.POST.get(str(i + 1700000000)))
            if request.POST.get(str(i + 1700000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_citacion=None)

            if request.POST.get(str(i + 1800000000)) != "":
                Denuncias.objects.filter(id=str(i)).update(fecha_inspeccion_terr=request.POST.get(str(i + 1800000000)))
            if request.POST.get(str(i + 1800000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_inspeccion_terr=None)

            if request.POST.get(str(i + 1900000000)) != "":
                Denuncias.objects.filter(id=str(i)).update(unidad_fiscalizada_terr=request.POST.get(str(i + 1900000000)))
            if request.POST.get(str(i + 1900000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(unidad_fiscalizada_terr=None)

            if request.POST.get(str(i + 2000000000)) != "":
                Denuncias.objects.filter(id=str(i)).update(fecha_inspeccion_rem=request.POST.get(str(i + 2000000000)))
            if request.POST.get(str(i + 2000000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_inspeccion_rem=None)

            if request.POST.get(str(i + 2100000000)) != "":
                Denuncias.objects.filter(id=str(i)).update(unidad_fiscalizada_rem=request.POST.get(str(i + 2100000000)))
            if request.POST.get(str(i + 2100000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(unidad_fiscalizada_rem=None)

            if request.POST.get(str(i + 2200000000)) != "":
                Denuncias.objects.filter(id=str(i)).update(fecha_inspeccion_sub=request.POST.get(str(i + 2200000000)))
            if request.POST.get(str(i + 2200000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_inspeccion_sub=None)

            if request.POST.get(str(i + 2300000000)) != "":
                Denuncias.objects.filter(id=str(i)).update(unidad_fiscalizada_sub=request.POST.get(str(i + 2300000000)))
            if request.POST.get(str(i + 2300000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(unidad_fiscalizada_sub=None)

            if request.POST.get(str(i + 2400000000)) != "":
                Denuncias.objects.filter(id=str(i)).update(fecha_requer=request.POST.get(str(i + 2400000000)))
            if request.POST.get(str(i + 2400000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_requer=None)

            if request.POST.get(str(i + 2500000000)) != "":
                Denuncias.objects.filter(id=str(i)).update(municipalidad=request.POST.get(str(i+2500000000)))
            if request.POST.get(str(i + 2500000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(municipalidad=None)

            if request.POST.get(str(i+9900000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_res_sad=request.POST.get(str(i+9900000000)))
            if request.POST.get(str(i +9900000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_res_sad=None)

            if request.POST.get(str(i+2600000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_sad=request.POST.get(str(i+2600000000)))
            if request.POST.get(str(i+2600000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_sad= None)

            if request.POST.get(str(i+2700000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_res_req=request.POST.get(str(i+2700000000)))
            if request.POST.get(str(i + 2700000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_res_req= None)

            if request.POST.get(str(i+2800000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_req=request.POST.get(str(i+2800000000)))
            if request.POST.get(str(i + 2800000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_req= None)

            if request.POST.get(str(i+2900000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_comparecencia=request.POST.get(str(i+2900000000)))
            if request.POST.get(str(i + 2900000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_comparecencia= None)

            if request.POST.get(str(i+3000000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_cit=request.POST.get(str(i+3000000000)))
            if request.POST.get(str(i + 3000000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_cit= None)

            if request.POST.get(str(i+3100000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_terr=request.POST.get(str(i+3100000000)))
            if request.POST.get(str(i+3100000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_terr= None)

            if request.POST.get(str(i+3200000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_rem=request.POST.get(str(i+3200000000)))
            if request.POST.get(str(i+3200000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_rem= None)

            if request.POST.get(str(i+3300000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_sub=request.POST.get(str(i+3300000000)))
            if request.POST.get(str(i+3300000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_sub= None)

            if request.POST.get(str(i+3400000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_orden_ret=request.POST.get(str(i+3400000000)))
            if request.POST.get(str(i+3400000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_orden_ret= None)

            if request.POST.get(str(i+3500000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_abogado=request.POST.get(str(i+3500000000)))
            if request.POST.get(str(i + 3500000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_abogado= None)

            if request.POST.get(str(i+3600000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(motivo_abogado=request.POST.get(str(i+3600000000)))
            if request.POST.get(str(i+3600000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(motivo_abogado= None)

            if request.POST.get(str(i+5400000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(obs_abogado=request.POST.get(str(i+5400000000)))
            if request.POST.get(str(i+5400000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(obs_abogado= None)


            try:
                if request.FILES[str(i + 4600000000)] != "":
                    myfile = request.FILES[str(i + 4600000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'SAD_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_sad=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 4700000000)] != "":
                    myfile = request.FILES[str(i + 4700000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'REQ_INF_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_req_inf=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 4800000000)] != "":
                    myfile = request.FILES[str(i + 4800000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'CIT_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_cit=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 4900000000)] != "":
                    myfile = request.FILES[str(i + 4900000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'INSP_TERR_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_ins_terr=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 5000000000)] != "":
                    myfile = request.FILES[str(i + 5000000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'INSP_REM_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_ins_rem=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 5100000000)] != "":
                    myfile = request.FILES[str(i + 5100000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'REQ_SUB_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_req_sub=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 5200000000)] != "":
                    myfile = request.FILES[str(i + 5200000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'ORD_RET_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_ord_ret=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            if request.POST.get(str("button_enviar")):
                Denuncias.objects.filter(id=str(i)).update(estado_jefe="RESULTADO_ABOGADO_DEVUELTO")
                return redirect("abogado_enviados")
            if request.POST.get(str("button_guardar")):
                return redirect("abogado_enviados")

    return render(request, 'GestionDenuncias/abogado_rechazo_validacion.html', context)

def jefe_resultado_denuncia(request, id_denuncia):


    denuncia_obj_6 = Denuncias.objects.filter(id=id_denuncia)
    context = {'todasdenuncias': denuncia_obj_6}

    if request.method == 'POST':
        for denuncia in denuncia_obj_6:
            i = denuncia.id
            if request.POST.get(str(i+9900000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_res_sad=request.POST.get(str(i+9900000000)))
            if request.POST.get(str(i + 9900000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_res_sad= None)

            if request.POST.get(str(i+2600000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_sad=request.POST.get(str(i+2600000000)))
            if request.POST.get(str(i + 2600000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_sad= None)

            if request.POST.get(str(i+2700000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_res_req=request.POST.get(str(i+2700000000)))
            if request.POST.get(str(i + 2700000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_res_req= None)

            if request.POST.get(str(i+2800000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_req=request.POST.get(str(i+2800000000)))
            if request.POST.get(str(i + 2800000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_req= None)

            if request.POST.get(str(i+2900000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(fecha_comparecencia=request.POST.get(str(i+2900000000)))
            if request.POST.get(str(i + 2900000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(fecha_comparecencia= None)

            if request.POST.get(str(i+3000000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_cit=request.POST.get(str(i+3000000000)))
            if request.POST.get(str(i + 3000000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_cit= None)

            if request.POST.get(str(i+3100000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_terr=request.POST.get(str(i+3100000000)))
            if request.POST.get(str(i+3100000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_terr= None)

            if request.POST.get(str(i+3200000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_rem=request.POST.get(str(i+3200000000)))
            if request.POST.get(str(i+3200000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_rem= None)

            if request.POST.get(str(i+3300000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_sub=request.POST.get(str(i+3300000000)))
            if request.POST.get(str(i+3300000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_insp_sub= None)

            if request.POST.get(str(i+3400000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_orden_ret=request.POST.get(str(i+3400000000)))
            if request.POST.get(str(i+3400000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_orden_ret= None)

            if request.POST.get(str(i+3500000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(resultado_abogado=request.POST.get(str(i+3500000000)))
            if request.POST.get(str(i + 3500000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(resultado_abogado= None)

            if request.POST.get(str(i+3600000000)) !="":
                Denuncias.objects.filter(id=str(i)).update(motivo_abogado=request.POST.get(str(i+3600000000)))
            if request.POST.get(str(i+3600000000)) == "":
                Denuncias.objects.filter(id=str(i)).update(motivo_abogado= None)

            try:
                if request.FILES[str(i + 4600000000)] != "":
                    myfile = request.FILES[str(i + 4600000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'SAD_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_sad=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 4700000000)] != "":
                    myfile = request.FILES[str(i + 4700000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'REQ_INF_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_req_inf=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 4800000000)] != "":
                    myfile = request.FILES[str(i + 4800000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'CIT_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_cit=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 4900000000)] != "":
                    myfile = request.FILES[str(i + 4900000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'INSP_TERR_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_ins_terr=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 5000000000)] != "":
                    myfile = request.FILES[str(i + 5000000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'INSP_REM_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_ins_rem=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 5100000000)] != "":
                    myfile = request.FILES[str(i + 5100000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'REQ_SUB_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_req_sub=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 5200000000)] != "":
                    myfile = request.FILES[str(i + 5200000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'ORD_RET_RESPUESTA_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_res_ord_ret=fs.save(nombre_archivo, myfile))
            except:
                print("no")

            try:
                if request.FILES[str(i + 5300000000)] != "":
                    myfile = request.FILES[str(i + 5300000000)]
                    folder = settings.MEDIA_ROOT
                    fs = FileSystemStorage(location=folder)
                    nombre_archivo = 'INFORME_' + myfile.name
                    Denuncias.objects.filter(id=str(i)).update(adjunto_informe=fs.save(nombre_archivo, myfile))
            except:
                print("no")


    return render(request, 'GestionDenuncias/jefe_resultados_denuncias.html', context)


def denuncias_enviadas_ad(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Denuncias.objects.all
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request, 'GestionDenuncias/admin_bandeja_ingresados.html', context)

def admin_despacho(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    denuncia_obj_3 = Denuncias.objects.filter(estado_jefe__icontains="DESPACHO")
    context = {'todasdenuncias': denuncia_obj_3}
    return render(request, 'GestionDenuncias/admin_despacho.html', context)



def modifica_denuncia(request):
    data = json.loads(request.body)

    if data['datos']['tipo'] == 'rechaza':
         Denuncias.objects.filter(id=str(data['datos']['id_denuncia'])).update(estado_jefe='DEVUELTO_JEFE')
         Denuncias.objects.filter(id=str(data['datos']['id_denuncia'])).update(obs_jefe=data['datos']['motivo_rechazo'])

    if data['datos']['tipo'] == 'acepta':
         Denuncias.objects.filter(id=str(data['datos']['id_denuncia'])).update(obs_jefe='ACEPTADO')
         if data['datos']['categoria'] == 'activa':
            Denuncias.objects.filter(id=str(data['datos']['id_denuncia'])).update(estado_jefe='ACTIVADO_DESPACHO')
         if data['datos']['categoria'] == 'desactiva':
            Denuncias.objects.filter(id=str(data['datos']['id_denuncia'])).update(estado_jefe='DESACTIVADO_DESPACHO')

    if data['datos']['tipo'] == 'acepta_masiva':
         Denuncias.objects.filter(codigo_desactivacion=str(data['datos']['id_denuncia'])).update(obs_jefe='ACEPTADO')
         Denuncias.objects.filter(codigo_desactivacion=str(data['datos']['id_denuncia'])).update(estado_jefe='DESACTIVADO_DESPACHO')
    if data['datos']['tipo'] == 'rechaza_masiva':
         Denuncias.objects.filter(codigo_desactivacion=str(data['datos']['id_denuncia'])).update(estado_jefe='DEVUELTO_JEFE')
         Denuncias.objects.filter(codigo_desactivacion=str(data['datos']['id_denuncia'])).update(obs_jefe=data['datos']['motivo_rechazo'])

    return JsonResponse([str(data['datos']['id_denuncia']), 'DEVUELTO_JEFE'], safe=False)

#from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth.decorators import login_required
from .views import *
from GestionRecursos.views import *
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), #Ok

#Rutas Administrador
    path('a/ingresom/', login_required(denuncias_ingreso), name='denuncias_ingreso'), #Ok
    path('a/ingresomas/', login_required(denuncias_ingreso_mass), name='denuncias_ingreso_mass'), #Ok
    path('a/enviados/', login_required(denuncias_enviadas_ad), name='denuncias_enviadas_ad'), #Ok
    path('a/despacho/', login_required(admin_despacho), name='admin_despacho'), #Ok

#Rutas Abogado
    path('ab/inicio/', login_required(abogado_inicio), name='abogado_inicio'), #Ok
    path('ab/evaluacion/', login_required(abogado_evaluacion), name='abogado_evaluacion'), #Ok
    path('ab/evaluaciondr/', login_required(abogado_evaluacion_dr), name='abogado_evaluacion_dr'), #Ok
    path('ab/evaluaciondr/<int:id_denuncia>/', login_required(abogado_evaluacion_dr_ver), name='abogado_evaluacion_dr_ver'), #Ok
    path('ab/rechazos/', login_required(abogado_rechazos), name='abogado_rechazos'), #Ok
    path('ab/comprobacion/', login_required(abogado_comprobacion), name='abogado_comprobacion'), #Ok
    path('ab/gestiones/act/<int:id_denuncia>/', login_required(abogado_gestion_denuncia_ac), name='gestion-denuncia_ac'), #Ok
    path('ab/gestiones/comp/<int:id_denuncia>/', login_required(gestion_denuncia_comp), name='gestion_denuncia_comp'), #Ok
    path('ab/gestiones/desact/<int:id_denuncia>/', login_required(abogado_gestion_denuncia_desac), name='gestion-denuncia_desac'), #Ok
    path('ab/enviados/', login_required(abogado_enviados), name='abogado_enviados'), #Ok

#Rutas Jefe
    path('j/inicio/', login_required(jefe_inicio), name='jefe_inicio'),  # Ok
    path('j/modifica_denuncia/', login_required(modifica_denuncia), name='modifica_denuncia'), # Ok
    path('j/evaluacion_act/', login_required(jefe_evaluacion_act), name='jefe_evaluacion_act'), # Ok
    path('j/evaluacion_desact/', login_required(jefe_evaluacion_desact), name='jefe_evaluacion_desact'), # Ok
    path('j/validacion_masiva/', login_required(validacion_masiva), name='validacion_masiva'), # Ok
    path('j/modifica_candidato/', login_required(modifica_candidato), name='modifica_candidato'), # Ok

#Rutas DR
    path('dr/evaluacion/', login_required(dr_evaluacion), name='dr_evaluacion'), #Ok
    path('dr/fiscalizacion/', login_required(dr_fiscalizacion), name='dr_fiscalizacion'), #Ok
    path('dr/resultadofiscalizacion/<int:id_denuncia>/', login_required(dr_resultadofiscalizacion), name='dr_resultadofiscalizacion'), #Ok
    path('dr/enviados/', login_required(dr_enviados), name='dr_enviados'), #Ok
    path('dr/evaluaciondr/<int:id_denuncia>/', login_required(dr_evaluacion_dr_ver),name='dr_evaluacion_dr_ver'),  # Ok
#Rutas SAR
    path('au/asignados/', login_required(auditor_bandeja_asignados), name='auditor_bandeja_asignados'),
    path('au/aportes/<int:rut>/', login_required(auditor_aportes), name='auditor_aportes'),
    path('au/cartola/<int:rut>/', login_required(auditor_cartola), name='auditor_cartola'),
    path('au/candidato/<int:rut>/', login_required(auditor_candidato), name='auditor_candidato'),
    path('au/ire/<int:eleccion>/', login_required(auditor_ire), name='auditor_ire'),
    path('au/avancegeneral/', login_required(auditor_avance_general), name='auditor_avance_general'),
    path('au/avancecelula/', login_required(auditor_avance_celula), name='auditor_avance_celula'),
    path('au/indicadores/', login_required(auditor_indicadores), name='auditor_indicadores'),
    path('au/f87/<int:rut>/', login_required(auditor_f87), name='auditor_f87'),
    path('au/f88/<int:rut>/', login_required(auditor_f88), name='auditor_f88'),

#Rutas SAR
    path('recursos/admin/total/', login_required(admin_recursos_total), name='admin_recursos_total'),
    path('recursos/admin/asigna/', login_required(admin_recursos_asigna), name='admin_recursos_asigna'),
    path('recursos/ld/asigna/', login_required(ld_recursos_asigna), name='ld_recursos_asigna'),
    path('recursos/admin/asignar_recurso/', login_required(asignar_recurso), name='asignar_recurso'), #P
    path('recursos/jc/asignar_recurso_lider/', login_required(asignar_recurso_lider), name='asignar_recurso_lider'), #P
    path('recursos/jc/asigna/', login_required(jc_recursos_asigna), name='jc_recursos_asigna'),
    path('recursos/jc/asignar_recurso_jc/', login_required(asignar_recurso_jc), name='asignar_recurso_jc'), #P
    path('recursos/au/informe_tecnico/', login_required(au_informe_tecnico), name='au_informe_tecnico'),
    path('recursos/au/pasar/', login_required(au_pasar_etapa), name='au_pasar_etapa'),  # P
    path('recursos/jc/valida_informe_tecnico/', login_required(jc_valida_informe_tecnico), name='jc_valida_informe_tecnico'),
    path('recursos/ab/ab_elabora_propuesta/', login_required(ab_elabora_propuesta), name='ab_elabora_propuesta'),
    path('recursos/jc/valida_propuesta/', login_required(jc_valida_propuesta), name='jc_valida_propuesta'),
    path('recursos/ab/valida_propuesta/', login_required(ab_valida_propuesta), name='ab_valida_propuesta'),
    path('recursos/ab/documentos/', login_required(formatosydocumentos), name='formatosydocumentos'),
    path('recursos/ld/valida_propuesta/', login_required(ld_valida_propuesta), name='ld_valida_propuesta'),
    path('recursos/jd/valida_propuesta/', login_required(jd_valida_propuesta), name='jd_valida_propuesta'),
    path('recursos/sd/valida_propuesta/', login_required(sd_valida_propuesta), name='sd_valida_propuesta'),
    path('recursos/xv/genera_expediente/', login_required(xv_genera_expediente), name='xv_genera_expediente'),
    path('recursos/xv/envia_tricel/', login_required(xv_envia_tricel), name='xv_envia_tricel'),
    path('recursos/xv/monitoreo_sentencia/', login_required(xv_monitoreo_sentencia), name='xv_monitoreo_sentencia'),
    path('recursos/gd/subir_a_firma/', login_required(gd_subir_a_firma), name='gd_subir_a_firma'),
    path('recursos/gd/en_firma_director/', login_required(gd_en_firma_director), name='gd_en_firma_director'),
    path('recursos/eb/pagos/', login_required(fin_revision_pagos), name='fin_revision_pagos'),
    path('recursos/reporte/', login_required(reporte_vista), name='reporte_vista'),
    path('recursos/envio_correo/', login_required(enviar_correo), name='enviar_correo'),
    path('recursos/gd/en_notificacion/', login_required(gd_en_notificacion), name='gd_en_notificacion'),
]

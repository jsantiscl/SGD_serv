
#from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth.decorators import login_required
from .views import *
from GestionRecursos.views import *
from AlertasFiscalizacion.views import *
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
    path('recursos/ab/asigna/', login_required(ab_recursos_asigna), name='ab_recursos_asigna'),
    path('recursos/admin/asignar_recurso/', login_required(asignar_recurso), name='asignar_recurso'), #P
    path('recursos/jc/asignar_recurso_lider/', login_required(asignar_recurso_lider), name='asignar_recurso_lider'), #P
    path('recursos/jc/ab_asignar_recurso_lider/', login_required(ab_asignar_recurso_lider), name='ab_asignar_recurso_lider'), #P
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
    path('recursos/ld/valida_propuesta_ac/', login_required(ld_valida_propuesta_ac), name='ld_valida_propuesta_ac'),
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
    path('recursos/gd/subir_sge/', login_required(gd_subir_sge), name='gd_subir_sge'),

    #Plebiscito
    path('plebiscito/total_solicitudes/', login_required(total_solicitudes), name='total_solicitudes'),
    path('plebiscito/asignacion_inscripciones/', login_required(asigna_admin_inscripciones), name='admin_recursos_asigna'),
    path('plebiscito/revision_inscripciones/', login_required(revision_inscripciones), name='revision_inscripciones'),
    path('plebiscito/par/<int:id_pleb>/', login_required(revisa_particular_pleb), name='revisa_particular_pleb'),
    path('plebiscito/revision_inscripciones/pasar/', login_required(pleb_pasar_etapa), name='pleb_pasar_etapa'),  # P

    # Fiscalizacion
    path('fiscalizacion/Alertas/', login_required(alertas), name='alertas'),
    path('fiscalizacion/AlertasAsignadas/', login_required(alertas_asignadas), name='alertas_asignadas'),
    path('fiscalizacion/BaseCompleta/', login_required(base_completa), name='base_completa'),
    path('fiscalizacion/detalle/<str:nombre>', login_required(detalle_base), name='detalle_base'),
    path('fiscalizacion/Alertas/pasar/', login_required(alarma_pasar_etapa), name='alarma_pasar_etapa'),  # P
    # APis
    path('recursos/api/prueba/', carga_datos, name='carga_datos'),  # P
    path('api/carga_datos_actas_terreno/', carga_datos_actas_terreno, name='carga_datos_actas_terreno'),  # P
    path('api/carga_datos_actas_remotas/', carga_datos_actas_remotas, name='carga_datos_actas_remotas'),  # P
    #Revisor
    path('revisor/terreno_pendiente_clasificacion/', login_required(terreno_pendiente_clasificacion), name='terreno_pendiente_clasificacion'),
    path('revisor/remota_pendiente_clasificacion/', login_required(remota_pendiente_clasificacion), name='remota_pendiente_clasificacion'),
    path('revisor/terreno_con_infraccion/', login_required(terreno_con_infraccion),
         name='terreno_con_infraccion'),
    path('revisor/remota_con_infraccion/', login_required(remotas_con_infraccion),
         name='remotas_con_infraccion'),
    path('pasar_acta/', pasar_acta, name='pasar_acta'),  # P
    path('revisor/terreno_archivo/', login_required(terreno_archivo),
         name='terreno_archivo'),
    path('revisor/remota_archivo/', login_required(remota_archivo),
         name='remota_archivo'),
    path('revisor/terreno_con_infraccion_gestiones/<str:id>', login_required(terreno_con_infraccion_gestiones),
         name='terreno_con_infraccion_gestiones'),
    path('revisor/remota_con_infraccion_gestiones/<str:id>', login_required(remota_con_infraccion_gestiones),
         name='remota_con_infraccion_gestiones'),
    path('efr/terreno_con_infraccion/', login_required(efr_terreno_con_infraccion),
         name='efr_terreno_con_infraccion'),
    path('efr/remota_con_infraccion/', login_required(efr_remota_con_infraccion),
         name='efr_remota_con_infraccion'),
    path('efr/terreno_con_infraccion_gestiones/<str:id>', login_required(efr_terreno_con_infraccion_gestiones),
         name='efr_terreno_con_infraccion_gestiones'),
    path('efr/remota_con_infraccion_gestiones/<str:id>', login_required(efr_remota_con_infraccion_gestiones),
         name='efr_remota_con_infraccion_gestiones'),
    path('revisor/terreno_con_infraccion_rechazo/', login_required(terreno_con_infraccion_rechazo),
         name='terreno_con_infraccion_rechazo'),
    path('revisor/terreno_con_infraccion_rechazo_gestiones/<str:id>', login_required(terreno_con_infraccion_rechazo_gestiones),
         name='terreno_con_infraccion_rechazo_gestiones'),
    path('revisor/remota_con_infraccion_rechazo/', login_required(remotas_con_infraccion_rechazo),
         name='remotas_con_infraccion_rechazo'),
    path('revisor/remota_con_infraccion_rechazo_gestiones/<str:id>',
         login_required(remota_con_infraccion_gestiones_rechazo),
         name='remota_con_infraccion_rechazo_gestiones'),

    path('expcsv/<str:lc>', expcsv, name='expcsv'),

    path('admin/terreno_con_infraccion/', login_required(admin_terreno_con_infraccion),
         name='admin_terreno_con_infraccion'),
    path('admin/remota_con_infraccion/', login_required(admin_remota_con_infraccion),
         name='admin_remota_con_infraccion'),
    path('abogado/evaluacion_terreno/', login_required(abogado_evaluacion_terreno),
         name='abogado_evaluacion_terreno'),
    path('abogado/activar_terreno/<str:id>', login_required(abogado_activar_terreno),
         name='abogado_activar_terreno'),
    path('abogado/desactivar_terreno/<str:id>', login_required(abogado_desactivar_terreno),
         name='abogado_desactivar_terreno'),
    path('abogado/evaluacion_remota/', login_required(abogado_evaluacion_remota),
         name='abogado_evaluacion_remota'),
    path('abogado/activar_remota/<str:id>', login_required(abogado_activar_remota),
         name='abogado_activar_remota'),
    path('abogado/desactivar_remota/<str:id>', login_required(abogado_desactivar_remota),
         name='abogado_desactivar_remota'),
    path('abogado/activadas_terreno/', login_required(abogado_activadas_terreno),
         name='abogado_activadas_terreno'),
    path('abogado/activadas_terreno_gestiones/<str:id>', login_required(abogado_activadas_terreno_gestiones),
         name='abogado_activadas_terreno_gestiones'),
    path('abogado/activadas_remotas/', login_required(abogado_activadas_remotas),
         name='abogado_activadas_remotas'),
    path('abogado/activadas_remotas_gestiones/<str:id>', login_required(abogado_activadas_remotas_gestiones),
         name='abogado_activadas_remotas_gestiones'),

    path('efr/remota_devuelto_abogado/', login_required(efr_remota_devuelto_abogado),
         name='efr_remota_devuelto_abogado'),

    path('efr/remota_devuelta_abogado_gestiones/<str:id>', login_required(efr_remota_devuelta_abogado_gestiones),
         name='efr_remota_devuelta_abogado_gestiones'),

    path('efr/terreno_devuelto_abogado/', login_required(efr_terreno_devuelto_abogado),
         name='efr_terreno_devuelto_abogado'),

    path('efr/terreno_devuelta_abogado_gestiones/<str:id>', login_required(efr_terreno_devuelta_abogado_gestiones),
         name='efr_terreno_devuelta_abogado_gestiones'),

        path('insert_token/', insert_token, name='insert_token'),

    path('encargado/terreno_revision/', login_required(encargado_terreno_revision),
         name='encargado_terreno_revision'),

    path('encargado/terreno_revision_gestiones/<str:id>', login_required(encargado_terreno_revision_gestiones),
         name='encargado_terreno_revision_gestiones'),

    path('encargado/remota_revision/', login_required(encargado_remota_revision),
         name='encargado_remota_revision'),

    path('encargado/remota_revision_gestiones/<str:id>', login_required(encargado_remota_revision_gestiones),
         name='encargado_remota_revision_gestiones'),

    path('encargado/remota_despacho/', login_required(encargado_remota_despacho),
         name='encargado_remota_despacho'),

    path('encargado/terreno_despacho/', login_required(encargado_terreno_despacho),
         name='encargado_terreno_despacho'),

    path('dr/terreno_reporte/', login_required(dr_terreno_reporte),
         name='dr_terreno_reporte'),

    path('dr/remota_reporte/', login_required(dr_remota_reporte),
         name='dr_remota_reporte'),

]


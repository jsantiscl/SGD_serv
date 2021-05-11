
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth.decorators import login_required

from .views import denuncias_ingreso, jefe_inicio, jefe_pendientes, jefe_enviados, jefe_pendientes_instruccion, abogado_inicio
from .views import abogado_gestiones, abogado_gestion_denuncia, abogado_resultados, abogado_resultado_denuncia, abogado_enviados, jefe_validacion
from .views import abogado_rechazo_denuncia, denuncias_enviadas_ad, jefe_resultado_denuncia, abogado_evaluacion, denuncias_ingreso_mass, abogado_gestion_denuncia_ac, abogado_gestion_denuncia_desac
from .views import abogado_comprobacion, gestion_denuncia_comp
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('a/ingresom/', login_required(denuncias_ingreso), name='denuncias_ingreso'),
    path('a/ingresomas/', login_required(denuncias_ingreso_mass), name='denuncias_ingreso_mass'),
    path('a/enviados/', login_required(denuncias_enviadas_ad), name='denuncias_enviadas_ad'),
    path('j/inicio/', login_required(jefe_inicio), name='jefe_inicio'),
    path('j/pendientes/', login_required(jefe_pendientes), name='jefe_pendientes'),
    path('j/pendientesi/', login_required(jefe_pendientes_instruccion), name='jefe_pendientes_i'),
    path('j/enviadas/', login_required(jefe_enviados), name='jefe_enviados'),
    path('ab/inicio/', login_required(abogado_inicio), name='abogado_inicio'),
    path('ab/gestiones/', login_required(abogado_gestiones), name='abogado_gestiones'),
    path('ab/evaluacion/', login_required(abogado_evaluacion), name='abogado_evaluacion'),
    path('ab/comprobacion/', login_required(abogado_comprobacion), name='abogado_comprobacion'),
    path('ab/gestiones/<int:id_denuncia>/', login_required(abogado_gestion_denuncia), name='gestion-denuncia'),
    path('ab/gestiones/act/<int:id_denuncia>/', login_required(abogado_gestion_denuncia_ac), name='gestion-denuncia_ac'),
    path('ab/gestiones/comp/<int:id_denuncia>/', login_required(gestion_denuncia_comp), name='gestion_denuncia_comp'),
    path('ab/gestiones/desact/<int:id_denuncia>/', login_required(abogado_gestion_denuncia_desac), name='gestion-denuncia_desac'),
    path('ab/resultados/', abogado_resultados, name='abogado_resultados'),
    path('ab/resultados/<int:id_denuncia>/', login_required(abogado_resultado_denuncia), name='resultado-denuncia'),
    path('ab/enviados/', login_required(abogado_enviados), name='abogado_enviados'),
    path('j/validacion/', login_required(jefe_validacion), name='jefe_validacion'),
    path('ab/rechazos/<int:id_denuncia>/', login_required(abogado_rechazo_denuncia), name='rechazo-denuncia'),
    path('j/resultados/<int:id_denuncia>/', login_required(jefe_resultado_denuncia), name='jefe_resultado_denuncia'),
]

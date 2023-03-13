from django.urls import path
from django.urls import include
from django.contrib.auth.decorators import login_required
from ConsultasSCGYFE.views import *
urlpatterns = [
    # Fiscalizacion
    path('total/', login_required(admin_consultas_total), name='total_consultas'),
    path('nuevas/', login_required(consultas_nuevas), name='consultas_nuevas'),
    path('respuesta/', login_required(consultas_respuesta), name='consultas_respuesta'),
    path('envio/', login_required(consultas_envio_respuestas), name='consultas_envio_respuestas'),
    path('pasar/', login_required(consultas_pasar_etapa), name='consultas_pasar_etapa'),
    path('responder/', login_required(consultas_responder), name='consultas_responder'),
]

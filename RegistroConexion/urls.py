from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar_horario, name='registrar_horario'),
    path('historial/', views.historial_marcaciones, name='historial_marcaciones'),
    path('unidad_horarios/', views.usuarios_unidad_horarios, name='usuarios_unidad_horarios'),
    path('autorizar_compensacion/', views.autorizar_compensacion, name='autorizar_compensacion'),
    path('reporte_compensado/', views.reporte_compensado, name='reporte_compensado'),
]

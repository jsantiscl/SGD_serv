from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar_horario, name='registrar_horario'),

]

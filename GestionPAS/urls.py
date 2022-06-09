
#from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), #Ok

#Rutas Administrador
    path('inicio/', login_required(pas_inicio), name='pas_inicio'), #Ok

]

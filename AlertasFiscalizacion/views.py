from django.shortcuts import render

from django.shortcuts import redirect
from datetime import datetime
from django.db.models import Count
from AlertasFiscalizacion.models import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404
# Create your views here.

from django.conf import settings
from django.core.mail import send_mail
from GestionDenuncias.forms import *

# Create your views here.
def alertas(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    alertas = AlertasMeta.objects.all()
    context = {'todasdenuncias': alertas}
    return render(request,'AlertasFiscalizacion/Alertas.html', context)
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from SistemaControlPreventivo.models import *

# Create your views here.
def admin_asignacion_candidato(request):
    # Consulta el grupo por su nombre
    group = Group.objects.get(name="AuditorControlPreventivo")

    # Obtiene todos los usuarios que pertenecen al grupo
    auditores = group.user_set.all()

    # Filtrar los candidatos como lo hacías antes
    candidatos = Candidatos.objects.filter(estado='1_Ingreso')

    # Agregar los auditores al contexto
    context = {'candidatos': candidatos, 'auditores': auditores}

    return render(request, 'SistemaControlPreventivo/SCP_Admin_Asignacion.html', context)
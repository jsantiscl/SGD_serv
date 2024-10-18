from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from .models import RegistroHorario
# Create your views here.

@login_required
def registrar_horario(request):
    usuario = request.user
    hora_actual = datetime.now()
    if request.method == 'POST':
        # Verifica si ya existe una entrada para hoy
        if RegistroHorario.entrada_existente_hoy(usuario):
            # No permitir registrar nuevamente si ya hay un registro hoy
            return render(request, 'RegistroConexion/registro.html', {
                'error': 'Ya has registrado tu entrada hoy. No puedes registrar nuevamente.'
            })

        # Registra la entrada
        tipo_trabajo = request.POST.get('modoTrabajo', 'Teletrabajo')
        registro = RegistroHorario(usuario=usuario, tipo_trabajo=tipo_trabajo)
        registro.registrar_entrada()

        #return redirect('pagina_exito')  # Redirige a una página de éxito después del registro

    return render(request, 'RegistroConexion/registro.html', {'hora_actual': hora_actual})

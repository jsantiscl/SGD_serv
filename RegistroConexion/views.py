from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UsuarioUnidad, RegistroHorario, JefaturaUnidad
from django.utils import timezone
from django.http import JsonResponse
from datetime import timedelta, datetime
import requests
from requests.exceptions import RequestException

@login_required
def registrar_horario(request):
    usuario = request.user
    hoy = timezone.now().date()

    # Recuperar registros del día actual
    entrada_hoy = RegistroHorario.objects.filter(usuario=usuario, tipo_e_o_s='Entrada', hora__date=hoy).first()
    salida_hoy = RegistroHorario.objects.filter(usuario=usuario, tipo_e_o_s='Salida', hora__date=hoy).first()

    if request.method == 'POST':
        tipo_e_o_s = request.POST.get('tipo_e_o_s')
        tipo_trabajo = request.POST.get('tipo_trabajo')

        if tipo_e_o_s == 'Entrada' and not entrada_hoy:
            # Registrar entrada si no hay una entrada registrada para hoy
            RegistroHorario.objects.create(
                usuario=usuario,
                hora=timezone.now(),
                tipo_e_o_s='Entrada',
                tipo_trabajo=tipo_trabajo
            )
        elif tipo_e_o_s == 'Salida' and entrada_hoy and not salida_hoy:
            # Registrar salida si hay una entrada registrada y no hay una salida para hoy
            RegistroHorario.objects.create(
                usuario=usuario,
                hora=timezone.now(),
                tipo_e_o_s='Salida',
                tipo_trabajo=entrada_hoy.tipo_trabajo  # Mantener el mismo tipo de trabajo que la entrada
            )

        return redirect('registrar_horario')

    return render(request, 'RegistroConexion/registro.html', {
        'entrada_hoy': entrada_hoy,
        'salida_hoy': salida_hoy,
        'hora_actual': timezone.now(),
    })


@login_required
def historial_marcaciones(request):
    usuario = request.user
    hoy = timezone.now().date()

    # Obtener registros de entrada y salida por fecha
    registros = RegistroHorario.objects.filter(usuario=usuario).order_by('-hora__date', '-hora')
    historial = {}

    for registro in registros:
        fecha = registro.hora.date()
        if fecha not in historial:
            historial[fecha] = {'entrada': None, 'salida': None, 'tipo_trabajo': registro.tipo_trabajo}

        if registro.tipo_e_o_s == 'Entrada':
            historial[fecha]['entrada'] = registro.hora
        elif registro.tipo_e_o_s == 'Salida':
            historial[fecha]['salida'] = registro.hora

    return render(request, 'RegistroConexion/historial.html', {'historial': historial})



@login_required
def usuarios_unidad_horarios(request):
    usuario = request.user

    # Verificar si el usuario es jefe de una unidad
    try:
        jefatura = JefaturaUnidad.objects.get(jefe=usuario)
    except JefaturaUnidad.DoesNotExist:
        return render(request, 'RegistroConexion/no_jefe.html')  # Muestra un mensaje si no es jefe

    # Obtener todos los usuarios de la unidad del jefe
    usuarios_unidad = UsuarioUnidad.objects.filter(unidad=jefatura.unidad)

    # Obtener festivos de la API
    url_festivos = "https://apis.digital.gob.cl/fl/feriados"
    festivos = []
    try:
        response = requests.get(url_festivos, timeout=5)  # Establece un tiempo de espera de 5 segundos
        if response.status_code == 200:
            festivos_data = response.json()
            # Convertir las fechas de los festivos a objetos de fecha
            festivos = [datetime.strptime(f['fecha'], "%Y-%m-%d").date() for f in festivos_data]
        else:
            print(f"Error al obtener los datos de la API. Código de estado: {response.status_code}")
    except RequestException as e:
        # Si hay un error de conexión o de solicitud, continuar sin datos de festivos
        print(f"Error al conectar con la API de Feriados: {e}")

    # Obtener registros de marcación de los usuarios de la unidad
    historial_unidad = []
    for usuario_unidad in usuarios_unidad:
        registros = RegistroHorario.objects.filter(usuario=usuario_unidad.usuario).order_by('-hora__date', '-hora')
        historial = {}
        for registro in registros:
            fecha = registro.hora.date()
            es_festivo = fecha in festivos

            if fecha not in historial:
                historial[fecha] = {
                    'usuario': usuario_unidad.usuario.get_full_name(),
                    'entrada': None,
                    'salida': None,
                    'tipo_trabajo': registro.tipo_trabajo,
                    'compensacion': '0h 0m',
                    'es_festivo': es_festivo
                }

            if registro.tipo_e_o_s == 'Entrada':
                historial[fecha]['entrada'] = registro.hora
            elif registro.tipo_e_o_s == 'Salida':
                historial[fecha]['salida'] = registro.hora

            # Calcular el tiempo potencialmente compensable
            if historial[fecha]['entrada'] and historial[fecha]['salida']:
                duracion = historial[fecha]['salida'] - historial[fecha]['entrada']
                horas_totales = duracion.total_seconds() // 3600
                minutos_totales = (duracion.total_seconds() % 3600) // 60

                if fecha.weekday() >= 5 or es_festivo:  # Sábado, domingo o festivo
                    historial[fecha]['compensacion'] = f'{int(horas_totales)}h {int(minutos_totales)}m'
                elif fecha.weekday() == 4:  # Viernes (más de 8 horas)
                    if horas_totales > 8:
                        horas_compensables = horas_totales - 8
                        historial[fecha]['compensacion'] = f'{int(horas_compensables)}h {int(minutos_totales)}m'
                else:  # Lunes a jueves (más de 9 horas)
                    if horas_totales > 9:
                        horas_compensables = horas_totales - 9
                        historial[fecha]['compensacion'] = f'{int(horas_compensables)}h {int(minutos_totales)}m'

        historial_unidad.append(historial)

    return render(request, 'RegistroConexion/usuarios_unidad_horarios.html', {
        'historial_unidad': historial_unidad,
        'unidad': jefatura.unidad
    })
@login_required
def autorizar_compensacion(request):
    if request.method == 'POST':
        registro_id = request.POST.get('registro_id')
        motivo = request.POST.get('motivo')

        try:
            registro = RegistroHorario.objects.get(id=registro_id)
            registro.compensacion_autorizada = True
            registro.motivo_compensacion = motivo
            registro.save()
            return JsonResponse({'success': True})
        except RegistroHorario.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Registro no encontrado'})

    return JsonResponse({'success': False, 'error': 'Método no permitido'})

@login_required
def reporte_compensado(request):
    usuario = request.user

    # Verificar si el usuario es jefe de una unidad
    try:
        jefatura = JefaturaUnidad.objects.get(jefe=usuario)
    except JefaturaUnidad.DoesNotExist:
        return render(request, 'RegistroConexion/no_jefe.html')  # Muestra un mensaje si no es jefe

    # Obtener todos los usuarios de la unidad del jefe
    usuarios_unidad = UsuarioUnidad.objects.filter(unidad=jefatura.unidad)

    # Calcular el reporte compensado para cada usuario
    reporte = []
    for usuario_unidad in usuarios_unidad:
        usuario = usuario_unidad.usuario
        registros = RegistroHorario.objects.filter(usuario=usuario, compensacion_autorizada=True)

        # Inicializar acumulador de tiempo compensado
        tiempo_compensado_total = timedelta()

        # Sumar el tiempo compensado de cada registro autorizado
        for registro in registros:
            if registro.hora_entrada and registro.hora_salida:
                duracion = registro.hora_salida - registro.hora_entrada
                dia_semana = registro.hora_entrada.weekday()

                # Verificar el tiempo compensado según el día de la semana
                if dia_semana >= 5:  # Sábado o domingo
                    tiempo_compensado_total += duracion
                elif dia_semana == 4:  # Viernes
                    if duracion > timedelta(hours=8):
                        tiempo_compensado_total += (duracion - timedelta(hours=8))
                else:  # Lunes a jueves
                    if duracion > timedelta(hours=9):
                        tiempo_compensado_total += (duracion - timedelta(hours=9))

        # Convertir el tiempo compensado total a horas y minutos
        horas_generadas = tiempo_compensado_total.total_seconds() // 3600
        minutos_generados = (tiempo_compensado_total.total_seconds() % 3600) // 60

        # Compensado utilizado (por ahora, 0)
        compensado_utilizado = 0

        # Compensado disponible
        compensado_disponible = tiempo_compensado_total - timedelta(minutes=compensado_utilizado)
        horas_disponibles = compensado_disponible.total_seconds() // 3600
        minutos_disponibles = (compensado_disponible.total_seconds() % 3600) // 60

        reporte.append({
            'usuario': usuario.get_full_name(),
            'compensado_generado': f'{int(horas_generadas)}h {int(minutos_generados)}m',
            'compensado_utilizado': '0h 0m',
            'compensado_disponible': f'{int(horas_disponibles)}h {int(minutos_disponibles)}m'
        })

    return render(request, 'RegistroConexion/reporte_compensado.html', {
        'reporte': reporte,
        'unidad': jefatura.unidad
    })
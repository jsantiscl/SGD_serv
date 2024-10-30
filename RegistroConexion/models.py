from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date

class RegistroHorario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    hora = models.DateTimeField(null=True, blank=True, default=None)
    tipo_e_o_s = models.CharField(max_length=10,
                                  choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')])
    tipo_trabajo = models.CharField(max_length=15,
                                    choices=[('Presencial', 'Presencial'), ('Teletrabajo', 'Teletrabajo')], default=None)
    compensacion_autorizada = models.BooleanField(default=False)
    motivo_compensacion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.usuario} - {self.hora} - {self.tipo_e_o_s} - {self.tipo_trabajo}'


    @staticmethod
    def registro_existente_hoy(usuario, tipo_e_o_s):
        """Verifica si el usuario ya tiene un registro de entrada o salida para hoy."""
        hoy = date.today()
        return RegistroHorario.objects.filter(usuario=usuario, tipo_e_o_s=tipo_e_o_s, hora__date=hoy).exists()
class Unidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class UsuarioUnidad(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='miembros')

    def __str__(self):
        return f'{self.usuario.username} - {self.unidad.nombre}'

class JefaturaUnidad(models.Model):
    unidad = models.OneToOneField(Unidad, on_delete=models.CASCADE, related_name='jefatura')
    jefe = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Jefe de {self.unidad.nombre}: {self.jefe.username}'
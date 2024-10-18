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
    def __str__(self):
        return f'{self.usuario} - {self.hora} - {self.tipo_e_o_s} - {self.tipo_trabajo}'

    @staticmethod
    def entrada_existente_hoy(usuario):
        """Verifica si el usuario ya tiene un registro de entrada para hoy."""
        hoy = date.today()
        return RegistroHorario.objects.filter(usuario=usuario, hora_entrada__date=hoy).exists()

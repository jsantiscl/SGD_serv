from django import forms
from .models import Denuncias,Abogados, Adjuntos
from django.forms import ClearableFileInput

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class DenunciasForm(forms.ModelForm):
    class Meta:
        model = Denuncias
        fields = [
        'numero',
        'fecha_ingreso',
        'via_de_ingreso',
        'nombre_denunciante',
        'nombre_denunciado',
        'tipo_de_denunciado',
        'elecciones',
        'candidatura',
        'territorio_electoral',
        'obs_ingreso',
        'adjunto_denuncia']
        widgets = {
            'adjunto_denuncia': ClearableFileInput(attrs={'multiple': True}),
        }

class ResumeUpload(forms.ModelForm):
    class Meta:
        model = Adjuntos
        fields = ['archivos']
        widgets = {
            'archivos': ClearableFileInput(attrs={'multiple': True}),
        }


from django import forms
from .models import Denuncias,Abogados, Adjuntos
from django.forms import ClearableFileInput

class DenunciasForm(forms.ModelForm):
    class Meta:
        model = Denuncias
        fields = [
        'numero',
        'link_adjuntos',
        'fecha_ingreso',
        'via_de_ingreso',
        'nombre_denunciante',
        'nombre_denunciado',
        'obs_ingreso',
        'abogado_asistente']
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'link_adjuntos': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'via_de_ingreso': forms.Select(attrs={'class': 'form-control'}),
            'nombre_denunciante': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_denunciado': forms.TextInput(attrs={'class': 'form-control'}),
           # 'tipo_de_denunciado': forms.Select(attrs={'class': 'form-control'}),
           # 'elecciones': forms.Select(attrs={'class': 'form-control'}),
           # 'candidatura': forms.Select(attrs={'class': 'form-control'}),
           # 'territorio_electoral': forms.TextInput(attrs={'class': 'form-control'}),
            'obs_ingreso': forms.Textarea(attrs={'class': 'form-control'}),
            'abogado_asistente': forms.Select(attrs={'class': 'form-control'}),
           # 'adjunto_denuncia': ClearableFileInput(attrs={'multiple': True}),
        }

class ResumeUpload(forms.ModelForm):
    class Meta:
        model = Adjuntos
        fields = ['archivos']
        widgets = {

            'archivos': ClearableFileInput(attrs={'multiple': True}),
        }

class UpdateDetailsForm(forms.Form):
 excel_file = forms.FileField(label='Subir Archivo', required=False)

class ActivaDenuncia(forms.ModelForm):
    class Meta:
        model = Denuncias
        fields = [

            'elecciones',
            'nombre_denunciado',

            'infraccion_denunciada',
            'plazo_investigacion',
            'tipo_diligencia',
            'obs_abogado',
            'guarda',
]
        widgets = {

            'elecciones': forms.Select(attrs={'class': 'form-control'}),
            'nombre_denunciado': forms.TextInput(attrs={'class': 'form-control'}),

            'infraccion_denunciada': forms.Select(attrs={'class': 'form-control'}),
            'plazo_investigacion': forms.Select(attrs={'class': 'form-control'}),
            'tipo_diligencia': forms.Select(attrs={'class': 'form-control'}),
            'obs_abogado': forms.Textarea(attrs={'class': 'form-control'}),
            'guarda': forms.HiddenInput(),
        }
        labels = {

            'elecciones' : 'Elecciones',
            'nombre_denunciado' : 'Nombre Denunciado',

            'infraccion_denunciada': 'Infracción Denunciada',
            'plazo_investigacion': 'Plazo de Investigación',
            'tipo_diligencia': 'Tipo Diligencia',
            'obs_abogado' : 'Observaciones Abogado',
            'guarda' : 'guarda',
        }

class DetallesDenuncia(forms.ModelForm):
    class Meta:
        model = Denuncias
        fields = [
            'numero',
            'link_adjuntos',
            'fecha_ingreso',
            #'via_de_ingreso',
            'nombre_denunciante',
            'nombre_denunciado',
            'obs_ingreso',
            #'abogado_asistente'
        ]
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'link_adjuntos': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'disabled': 'True'}),
            #'via_de_ingreso': forms.Select(attrs={'class': 'form-control', 'disabled': 'True'}),
            'nombre_denunciante': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'nombre_denunciado': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            # 'tipo_de_denunciado': forms.Select(attrs={'class': 'form-control'}),
            # 'elecciones': forms.Select(attrs={'class': 'form-control'}),
            # 'candidatura': forms.Select(attrs={'class': 'form-control'}),
            # 'territorio_electoral': forms.TextInput(attrs={'class': 'form-control'}),
            'obs_ingreso': forms.Textarea(attrs={'class': 'form-control', 'disabled': 'True'}),
        #    'abogado_asistente': forms.Select(attrs={'class': 'form-control', 'disabled': 'True'}),
        # 'adjunto_denuncia': ClearableFileInput(attrs={'multiple': True}),

        }



class DesactivaDenuncia(forms.ModelForm):
    class Meta:
        model = Denuncias
        fields = [

            'elecciones',
            'nombre_denunciado',

            'codigo_desactivacion',
            'obs_abogado',
            'guarda',
]
        widgets = {

            'elecciones': forms.Select(attrs={'class': 'form-control'}),
            'nombre_denunciado': forms.TextInput(attrs={'class': 'form-control'}),

            'codigo_desactivacion': forms.Select(attrs={'class': 'form-control'}),
            'obs_abogado': forms.Textarea(attrs={'class': 'form-control'}),
            'guarda': forms.HiddenInput(),
        }
        labels = {

            'elecciones' : 'Elecciones',
            'nombre_denunciado' : 'Nombre Denunciado',

            'codigo_desactivacion': 'Codigo Desactivacion',
            'obs_abogado' : 'Observaciones Abogado',
            'guarda': 'guarda',
        }



class CompruebaDenuncia(forms.ModelForm):
    class Meta:
        model = Denuncias
        fields = [

            'elecciones',
            'nombre_denunciado',

            'infraccion_denunciada',
            'plazo_investigacion',
            'tipo_diligencia',
            'resultado_comprobacion',
            'obs_abogado',
            'guardac',
        ]
        widgets = {

            'elecciones': forms.Select(attrs={'class': 'form-control', 'disabled': 'true'}),
            'nombre_denunciado': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'true'}),

            'infraccion_denunciada': forms.Select(attrs={'class': 'form-control', 'disabled': 'true'}),
            'plazo_investigacion': forms.Select(attrs={'class': 'form-control', 'disabled': 'true'}),
            'tipo_diligencia': forms.Select(attrs={'class': 'form-control', 'disabled': 'true'}),
            'resultado_comprobacion': forms.Select(attrs={'class': 'form-control'}),
            'obs_abogado': forms.Textarea(attrs={'class': 'form-control'}),
            'guardac': forms.HiddenInput(),
        }
        labels = {

            'elecciones': 'Elecciones',
            'nombre_denunciado': 'Nombre Denunciado',

            'infraccion_denunciada': 'Infracción Denunciada',
            'plazo_investigacion': 'Plazo de Investigación',
            'tipo_diligencia': 'Tipo Diligencia',
            'resultado_comprobacion': 'Resultado Comprobación',
            'obs_abogado': 'Observaciones Abogado',
            'guardac': 'guardac',
        }
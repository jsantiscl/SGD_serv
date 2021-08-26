from django import forms
from .models import Denuncias, Abogados
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
        'abogado_asistente',
        'asignacion_dr']
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'link_adjuntos': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'via_de_ingreso': forms.Select(attrs={'class': 'form-control'}),
            'nombre_denunciante': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_denunciado': forms.TextInput(attrs={'class': 'form-control'}),
            'obs_ingreso': forms.Textarea(attrs={'class': 'form-control'}),
            'abogado_asistente': forms.Select(attrs={'class': 'form-control'}),
            'asignacion_dr': forms.Select(attrs={'class': 'form-control'}),

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

            'nombre_denunciante',
            'nombre_denunciado',
            'obs_ingreso',

        ]
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'link_adjuntos': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'disabled': 'True'}),
            'nombre_denunciante': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'nombre_denunciado': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'obs_ingreso': forms.Textarea(attrs={'class': 'form-control', 'disabled': 'True'}),


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

            'infraccion_denunciada': forms.Select(attrs={'class': 'form-control'}),
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


class FiscalizacionDR(forms.ModelForm):
    class Meta:
        model = Denuncias
        fields = [
            'dr_id_inspeccion_survey',
            'dr_link_carpeta_fiscalizacion',
            'dr_nro_requerimiento_candidato' ,
            'dr_fecha_requerimiento_candidato',
            'dr_resultado_requerimiento_candidato',
            'dr_retiro_municipio',
            'dr_fecha_retiro_municipio',
            'dr_obs_fisca',
            'dr_guardac',
        ]
        widgets = {
            'dr_id_inspeccion_survey': forms.TextInput(attrs={'class': 'form-control',}),
            'dr_link_carpeta_fiscalizacion': forms.TextInput(attrs={'class': 'form-control'}),
            'dr_nro_requerimiento_candidato': forms.TextInput(attrs={'class': 'form-control'}),
            'dr_fecha_requerimiento_candidato': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dr_resultado_requerimiento_candidato': forms.Select(attrs={'class': 'form-control'}),
            'dr_retiro_municipio': forms.TextInput(attrs={'class': 'form-control'}),
            'dr_fecha_retiro_municipio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dr_obs_fisca': forms.TextInput(attrs={'class': 'form-control'}),
            'dr_guardac': forms.HiddenInput(),
        }
        labels = {

            'dr_id_inspeccion_survey': 'ID Inspeccion(ID Survey)',
            'dr_link_carpeta_fiscalizacion': 'Link Carpeta Fiscalizacion',
            'dr_nro_requerimiento_candidato': 'N° Requerimiento Candidato',
            'dr_fecha_requerimiento_candidato': 'Fecha Requerimiento Candidato',
            'dr_resultado_requerimiento_candidato': 'Resultado Requerimiento Candidato',
            'dr_retiro_municipio': 'N° Retiro Municipio',
            'dr_fecha_retiro_municipio': 'Fecha Retiro Municipio',
            'dr_obs_fisca': 'Observaciones',
            'dr_guardac': 'dr_guardac',
        }

class VerFiscalizacionDR(forms.ModelForm):
    class Meta:
        model = Denuncias
        fields = [
            'dr_id_inspeccion_survey',
            'dr_link_carpeta_fiscalizacion',
            'dr_nro_requerimiento_candidato' ,
            'dr_fecha_requerimiento_candidato',
            'dr_resultado_requerimiento_candidato',
            'dr_retiro_municipio',
            'dr_fecha_retiro_municipio',
            'dr_obs_fisca',
            'dr_guardac',
        ]
        widgets = {
            'dr_id_inspeccion_survey': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'true'}),
            'dr_link_carpeta_fiscalizacion': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'true'}),
            'dr_nro_requerimiento_candidato': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'true'}),
            'dr_fecha_requerimiento_candidato': forms.DateInput(attrs={'class': 'form-control', 'disabled': 'true'}),
            'dr_resultado_requerimiento_candidato': forms.Select(attrs={'class': 'form-control', 'disabled': 'true'}),
            'dr_retiro_municipio': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'true'}),
            'dr_fecha_retiro_municipio': forms.DateInput(attrs={'class': 'form-control', 'disabled': 'true'}),
            'dr_obs_fisca': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'true'}),
            'dr_guardac': forms.HiddenInput(),
        }
        labels = {

            'dr_id_inspeccion_survey': 'ID Inspeccion(ID Survey)',
            'dr_link_carpeta_fiscalizacion': 'Link Carpeta Fiscalizacion',
            'dr_nro_requerimiento_candidato': 'N° Requerimiento Candidato',
            'dr_fecha_requerimiento_candidato': 'Fecha Requerimiento Candidato',
            'dr_resultado_requerimiento_candidato': 'Resultado Requerimiento Candidato',
            'dr_retiro_municipio': 'N° Retiro Municipio',
            'dr_fecha_retiro_municipio': 'Fecha Retiro Municipio',
            'dr_obs_fisca': 'Observaciones',
            'dr_guardac': 'dr_guardac',
        }

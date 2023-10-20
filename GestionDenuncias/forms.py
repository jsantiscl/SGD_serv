from django import forms
from .models import Denuncias, Abogados, ActasTerreno, ActasRemotas
from GestionRecursos.models import *
from django.forms import ClearableFileInput
from django.db.models.functions import Concat
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
            'motivo_dr',
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
            'motivo_dr': forms.TextInput(attrs={'class': 'form-control'}),
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
            'motivo_dr': 'Observaciones',
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
            'motivo_dr',
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
            'motivo_dr': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'true'}),
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
            'motivo_dr': 'Observaciones',
            'dr_guardac': 'dr_guardac',
        }

class DetallesInscripcion(forms.ModelForm):
    class Meta:
        model = InscripcionesPlebiscito

        fields = [
            'tipo',
            'nombre_sol',
            'paterno_sol',
            'materno_sol',
            'rut_sol',
            'dv_sol',
            'nombre_org',
            'rut_orga',
            'dv_orga',
            'nombre_repr',
            'paterno_repr',
            'materno_repr',
            'rut_repr',
            'dv_repr',
            'participara_forma',
            'organizacion',
            'fecha_envio',

        ]
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'nombre_sol': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'paterno_sol': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'materno_sol': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'rut_sol': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'dv_sol': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'nombre_org': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'rut_orga': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'dv_orga': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'nombre_repr': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'paterno_repr': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'materno_repr': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'rut_repr': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'dv_repr': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'participara_forma': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'organizacion': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'True'}),
            'fecha_envio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'disabled': 'True'}),

        }

class RevisaCasos(forms.ModelForm):
    class Meta:
        model = RevisionesInscripciones

        fields = [


        'valida_adjunto',
        'valida_sin_fines_de_lucro',
        'propuesta',
        'comentarios_revisor',

        ]
        widgets = {
            'valida_adjunto': forms.Select(attrs={'class': 'form-control'}),
            'valida_sin_fines_de_lucro': forms.Select(attrs={'class': 'form-control'}),
            'propuesta': forms.Select(attrs={'class': 'form-control'}),
            'comentarios_revisor': forms.Textarea(attrs={'class': 'form-control'}),
        }


class GestionTerreno(forms.ModelForm):
    class Meta:
        model = ActasTerreno
        fields = [

            'sis_codigo',
            'sis_link',
            'sis_nro_requerimiento',
            'sis_fe_sub',
            'sis_plazo_respuesta',
            'sis_respuesta',
            'sis_oficio_retiro',
            'sis_certificado',
            'sis_propuesta',
            'sis_motivo',
            'sis_clasificacion',

]
        widgets = {

            'sis_codigo': forms.Select(attrs={'class': 'form-control'}),
            'sis_link': forms.TextInput(attrs={'class': 'form-control'}),
            'sis_nro_requerimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'sis_fe_sub': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sis_plazo_respuesta': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sis_respuesta': forms.Select(attrs={'class': 'form-control'}),
            'sis_oficio_retiro': forms.TextInput(attrs={'class': 'form-control'}),
            'sis_certificado': forms.TextInput(attrs={'class': 'form-control'}),
            'sis_propuesta': forms.Select(attrs={'class': 'form-control'}),
            'sis_motivo': forms.Textarea(attrs={'class': 'form-control'}),
            'sis_clasificacion': forms.HiddenInput(),

        }
        labels = {

            'sis_codigo' : 'Codigo',
            'sis_link' : 'Indicar Link Carpeta Sharepoint*',
            'sis_nro_requerimiento': 'Número Requerimiento:',
            'sis_fe_sub' : 'Fecha de requerimiento de subsanación:',
            'sis_plazo_respuesta': 'Plazo de Respuesta:',
            'sis_respuesta': 'Respuesta:',
            'sis_oficio_retiro': 'Oficio retiro al municipio:',
            'sis_certificado': 'Certificado:',
            'sis_propuesta': 'Propuesta*:',
            'sis_motivo': 'Motivo Revisor*:',
            'sis_clasificacion':'sis_clasificacion'

        }

class GestionRemota(forms.ModelForm):
    class Meta:
        model = ActasRemotas
        fields = [

            'sis_codigo',
            'sis_link',
            'sis_nro_requerimiento',
            'sis_fe_sub',
            'sis_plazo_respuesta',
            'sis_respuesta',
            'sis_oficio_retiro',
            'sis_certificado',
            'sis_propuesta',
            'sis_motivo',
            'sis_clasificacion',

]
        widgets = {

            'sis_codigo': forms.Select(attrs={'class': 'form-control'}),
            'sis_link': forms.TextInput(attrs={'class': 'form-control'}),
            'sis_nro_requerimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'sis_fe_sub': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sis_plazo_respuesta': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sis_respuesta': forms.Select(attrs={'class': 'form-control'}),
            'sis_oficio_retiro': forms.TextInput(attrs={'class': 'form-control'}),
            'sis_certificado': forms.TextInput(attrs={'class': 'form-control'}),
            'sis_propuesta': forms.Select(attrs={'class': 'form-control'}),
            'sis_motivo': forms.Textarea(attrs={'class': 'form-control'}),
            'sis_clasificacion': forms.HiddenInput(),

        }
        labels = {

            'sis_codigo' : 'Codigo',
            'sis_link' : 'Indicar Link Carpeta Sharepoint*',
            'sis_nro_requerimiento': 'Número Requerimiento:',
            'sis_fe_sub' : 'Fecha de requerimiento de subsanación:',
            'sis_plazo_respuesta': 'Plazo de Respuesta:',
            'sis_respuesta': 'Respuesta:',
            'sis_oficio_retiro': 'Oficio retiro al municipio:',
            'sis_certificado': 'Certificado:',
            'sis_propuesta': 'Propuesta*:',
            'sis_motivo': 'Motivo Revisor*:',
            'sis_clasificacion':'sis_clasificacion'

        }

class GestionTerrenoEFR(forms.ModelForm):
    class Meta:
        model = ActasTerreno
        fields = [

            'sis_codigo',
            'sis_link',
            'sis_nro_requerimiento',
            'sis_fe_sub',
            'sis_plazo_respuesta',
            'sis_respuesta',
            'sis_oficio_retiro',
            'sis_certificado',
            'sis_propuesta',
            'sis_motivo',
            'sis_resultado_efr',
            'sis_motivo_rechazo',
            'sis_clasificacion',

]
        widgets = {

            'sis_codigo': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_link': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'sis_nro_requerimiento': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_fe_sub': forms.DateInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_plazo_respuesta': forms.DateInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_respuesta': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_oficio_retiro': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_certificado': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_propuesta': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_motivo': forms.Textarea(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_resultado_efr': forms.Select(attrs={'class': 'form-control'}),
            'sis_motivo_rechazo': forms.Textarea(attrs={'class': 'form-control', }),
            'sis_clasificacion': forms.HiddenInput(),

        }
        labels = {

            'sis_codigo' : 'Codigo',
            'sis_link' : 'Indicar Link Carpeta Sharepoint*',
            'sis_nro_requerimiento': 'Número Requerimiento:',
            'sis_fe_sub' : 'Fecha de requerimiento de subsanación:',
            'sis_plazo_respuesta': 'Plazo de Respuesta:',
            'sis_respuesta': 'Respuesta:',
            'sis_oficio_retiro': 'Oficio retiro al municipio:',
            'sis_certificado': 'Certificado:',
            'sis_propuesta': 'Propuesta*:',
            'sis_motivo': 'Motivo Revisor*:',
            'sis_resultado_efr': 'Validacion Resultado',
            'sis_motivo_rechazo': 'Motivo Rechazo:',
            'sis_clasificacion':'sis_clasificacion'

        }

class GestionRemotasEFR(forms.ModelForm):
    class Meta:
        model = ActasRemotas
        fields = [

            'sis_codigo',
            'sis_link',
            'sis_nro_requerimiento',
            'sis_fe_sub',
            'sis_plazo_respuesta',
            'sis_respuesta',
            'sis_oficio_retiro',
            'sis_certificado',
            'sis_propuesta',
            'sis_motivo',
            'sis_resultado_efr',
            'sis_motivo_rechazo',
            'sis_clasificacion',

]
        widgets = {

            'sis_codigo': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_link': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'sis_nro_requerimiento': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_fe_sub': forms.DateInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_plazo_respuesta': forms.DateInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_respuesta': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_oficio_retiro': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_certificado': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_propuesta': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_motivo': forms.Textarea(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sis_resultado_efr': forms.Select(attrs={'class': 'form-control'}),
            'sis_motivo_rechazo': forms.Textarea(attrs={'class': 'form-control', }),
            'sis_clasificacion': forms.HiddenInput(),

        }
        labels = {

            'sis_codigo' : 'Codigo',
            'sis_link' : 'Indicar Link Carpeta Sharepoint*',
            'sis_nro_requerimiento': 'Número Requerimiento:',
            'sis_fe_sub' : 'Fecha de requerimiento de subsanación:',
            'sis_plazo_respuesta': 'Plazo de Respuesta:',
            'sis_respuesta': 'Respuesta:',
            'sis_oficio_retiro': 'Oficio retiro al municipio:',
            'sis_certificado': 'Certificado:',
            'sis_propuesta': 'Propuesta*:',
            'sis_motivo': 'Motivo Revisor*:',
            'sis_resultado_efr': 'Validacion Resultado',
            'sis_motivo_rechazo': 'Motivo Rechazo:',
            'sis_clasificacion':'sis_clasificacion'

        }


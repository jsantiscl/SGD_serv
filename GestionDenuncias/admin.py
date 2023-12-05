from django.contrib import admin

# Register your models here.
from .models import *
from GestionRecursos.models import *
from GestionPAS.models import *
from AlertasFiscalizacion.models import *
from ConsultasSCGYFE.models import *

class DenunciasAdmin(admin.ModelAdmin):
    search_fields = ['Numero']  # Puedes agregar más campos separados por comas

admin.site.register(Denuncias, DenunciasAdmin)
admin.site.register(Abogados)
admin.site.register(DireccionesRegionales)
admin.site.register(EncargadosRegionales)

admin.site.register(Recursos)
admin.site.register(UsersRecursos)
admin.site.register(Bitacora)
admin.site.register(UsersPlebiscito)
admin.site.register(InscripcionesPlebiscito)
admin.site.register(SociosInscritos)

admin.site.register(UsersFiscalizacion)
admin.site.register(AlertasMeta)
admin.site.register(AnunciosMeta)

admin.site.register(ConsultasFormulario)

admin.site.register(RevisoresDR)
admin.site.register(EFRDR)


class ActasTerrenoAdmin(admin.ModelAdmin):  ##Esto permite buscar por estos campos en el menu admin
    search_fields = ['id_inspeccion']  # Puedes agregar más campos separados por comas
class ActasRemotasAdmin(admin.ModelAdmin): ##Esto permite buscar por estos campos en el menu admin
    search_fields = ['id_inspeccion']  # Puedes agregar más campos separados por comas
admin.site.register(ActasTerreno, ActasTerrenoAdmin)
admin.site.register(ActasRemotas, ActasRemotasAdmin)
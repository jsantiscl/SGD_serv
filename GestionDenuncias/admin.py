from django.contrib import admin

# Register your models here.
from .models import *
from GestionRecursos.models import *
from GestionPAS.models import *
from AlertasFiscalizacion.models import *

admin.site.register(Denuncias)
admin.site.register(Abogados)
admin.site.register(DireccionesRegionales)
admin.site.register(EncargadosRegionales)
admin.site.register(Ire)
admin.site.register(Auditores)
admin.site.register(Aportes)
admin.site.register(Cartola)
admin.site.register(Recursos)
admin.site.register(UsersRecursos)
admin.site.register(Bitacora)
admin.site.register(UsersPlebiscito)
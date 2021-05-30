from django.contrib import admin

# Register your models here.
from .models import Denuncias,Abogados, Ire, Auditores, Aportes

admin.site.register(Denuncias)
admin.site.register(Abogados)
admin.site.register(Ire)
admin.site.register(Auditores)
admin.site.register(Aportes)
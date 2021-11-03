from django.contrib import admin
from .models import Agenda, Sucursal, Especialidad, Medico, Persona, Comuna, Region, Pago

admin.site.register(Agenda)
admin.site.register(Sucursal)
admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(Persona)
admin.site.register(Comuna)
admin.site.register(Pago)
admin.site.register(Region)


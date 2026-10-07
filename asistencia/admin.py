from django.contrib import admin
from .models import RegistroAsistencia

# Configuración del panel de administración
class asistenciaadmin(admin.ModelAdmin):
    list_display = ['id', 'nombres', 'apellidos', 'documento', 'fecha', 'asistio']
    search_fields = ['documento', 'nombres']
    list_filter = ['asistio', 'fecha']

admin.site.register(RegistroAsistencia, asistenciaadmin)
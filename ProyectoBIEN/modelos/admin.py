# modelos/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Comentario, Reserva, Tours
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombre', 'apellidos', 'is_staff', 'is_superuser')
    search_fields = ('email', 'nombre', 'apellidos')

admin.site.register(Usuario, UsuarioAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'created', 'coment')

admin.site.register(Comentario, ComentarioAdmin)


class AdministrarReserva(admin.ModelAdmin):
    readonly_fields = ('created','id')  
    list_display = ('nombre', 'personas', 'apellidos', 'telefono', 'edad', 'fecha','personas')  
    date_hierarchy = 'fecha'  

admin.site.register(Reserva, AdministrarReserva)

class AdministrarTours(admin.ModelAdmin):
    list_display = ('destino', 'precio')  # Adjust as needed
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id', 'updated')

admin.site.register(Tours, AdministrarTours)
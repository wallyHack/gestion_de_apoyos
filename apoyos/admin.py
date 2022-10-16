from django.contrib import admin

# Register your models here.
from .models import Apoyos, Departamento, EncargadoRuta, Localidad, Persona


class LocalidadAdmin(admin.ModelAdmin):
    """ modelelo administrativo de Localidad"""
    ordering = ['id']
    list_display = ('id', 'nombre', 'seccion', 'numero_habitantes')
    list_filter = ['nombre', 'seccion']
    search_fields = ['id', 'nombre']
    list_per_page = 10   
    
class DepartamentoAdmin(admin.ModelAdmin):
    """ modelo administrativo de Departamento"""
    ordering = ['id']
    list_display = ('id', 'nombre', 'numero_de_empleados')
    list_filter = ['nombre']
    search_fields = ['id', 'nombre']
    list_per_page = 10
    
class EncargadoRutaAdmin(admin.ModelAdmin):
    """ modelo administrativo de EnccargadoRuta"""
    ordering = ['id']
    list_display = ('id', 'nombres', 'ap_paterno', 'ap_materno', 'departamento', 'sexo', 'telefono', 'domicilio', 'email')
    list_filter = ['nombres', 'departamento', 'sexo']
    search_fields = ['id', 'nombres', 'ap_paterno']
    list_per_page = 8
    
class ApoyosAdmin(admin.ModelAdmin):
    """ modelo administrativo de Apoyos"""
    ordering = ['id']
    list_display = ('id', 'tipo', 'descripcion', 'fecha_de_entrega', 'notas_adicionales', 'persona', 'encargado_de_ruta')
    list_filter = ['persona', 'fecha_de_entrega', 'tipo', 'encargado_de_ruta']
    search_fields = ['id', 'tipo', 'descripcion']
    list_per_page = 8
    
class PersonaAdmin(admin.ModelAdmin):
    """ modelo administrativo de Persona"""
    ordering = ['id']
    list_display = ('id', 'nombres', 'ap_paterno', 'ap_materno', 'tipo', 'domicilio', 'estado', 'telefono', 'localidad')
    list_filter = ['tipo', 'estado', 'localidad']
    search_fields = ['id', 'nombres', 'ap_paterno']
    list_per_page = 12

admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Apoyos, ApoyosAdmin)
admin.site.register(EncargadoRuta, EncargadoRutaAdmin)
admin.site.register(Persona, PersonaAdmin)
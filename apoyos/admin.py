
from django.contrib import admin

# Register your models here.
from .models import Localidad, Apoyos, Persona, EncargadoRuta

class LocalidadAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'nombre', 'seccion', 'numero_habitantes')
    list_filter = ['nombre', 'seccion']
    search_fields = ['id', 'nombre']
    list_per_page = 10

class EncargadoRutaAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'nombres', 'ap_paterno', 'ap_materno', 'sexo', 'telefono', 'domicilio', 'email')
    list_filter = ['nombres', 'ap_paterno', 'sexo']
    search_fields = ['id', 'nombres', 'ap_paterno']
    list_per_page = 8

class ApoyosAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'tipo', 'descripcion', 'fecha_de_entrega', 'comprobacion', 'notas_adicionales', 'persona', 'persona_que_entrego')
    list_filter = ['persona', 'fecha_de_entrega', 'tipo']
    search_fields = ['id', 'tipo', 'descripcion']
    list_per_page = 8

class PersonaAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'nombres', 'ap_paterno', 'ap_materno', 'tipo', 'domicilio', 'estado', 'telefono', 'localidad')
    list_filter = ['id', 'nombres', 'ap_paterno', 'estado', 'localidad']
    search_fields = ['id', 'nombres', 'ap_paterno']
    list_per_page = 8

admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Apoyos, ApoyosAdmin)
admin.site.register(EncargadoRuta, EncargadoRutaAdmin)
admin.site.register(Persona, PersonaAdmin)
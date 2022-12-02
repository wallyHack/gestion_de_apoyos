from django.contrib import admin
from .models import Contribuyente

# Register your models here.
class ContribuyenteAdmin(admin.ModelAdmin):
    """ modelo administrativo de contribuyente """
    ordering = ['id']
    list_display = ('id', 'nombre', 'ap_paterno', 'ap_materno', 'genero', 'localidad', 'notas_adicionales')
    list_filter = ['localidad', 'genero']
    search_fields = ['id', 'nombre', 'localidad']
    list_per_page = 10
    
admin.site.register(Contribuyente, ContribuyenteAdmin)
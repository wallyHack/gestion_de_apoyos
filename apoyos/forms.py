
from django import forms
from .models import Localidad, Persona

class LocalidadesForm(forms.ModelForm):
    """ form para Localidades"""
    class Meta:
        model = Localidad
        #fields = '__all__'

        # campos que muestra el formulario
        fields = ("nombre", "seccion", "tipo")
        exclude = ['numero_habitantes']

    def __init__(self, *args, **kwargs):
        """ método que itera los campos del form y agrega la clase form-control de bootstrap a los input"""
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
class PersonasForm(forms.ModelForm):
    """ form para personas"""
    class Meta:
        model = Persona
        # campos que muestra el formulario
        fields = ("nombres", "ap_paterno", "ap_materno", "tipo", "genero", \
            "domicilio", "estado", "telefono", "localidad")
        
    def __init__(self, *args, **kwargs):
        """ método que itera los campos del form y agrega la clase form-control de bootstrap a los input"""
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

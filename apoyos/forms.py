
from dataclasses import field
from django import forms
from .models import Localidad, Persona, EncargadoRuta

class LocalidadesForm(forms.ModelForm):
    """ form para Localidades"""
    class Meta:
        model = Localidad
        #fields = '__all__'

        # campos que muestra el formulario
        fields = ("nombre", "seccion", "tipo")
        labels = {"nombre": "Nombre", "seccion": "Sección", "tipo": "Tipo"}
        exclude = ['numero_habitantes']
        widget = {'nombre': forms.TextInput}

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
        labels = {
            'nombres': 'Nombres', 'ap_paterno': 'Apellido Paterno', 'ap_materno': 'Apellido Materno',
            'genero': 'Género'
        }
        
    def __init__(self, *args, **kwargs):
        """ método que itera los campos del form y agrega la clase form-control de bootstrap a los input"""
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
class EncargadosRutaForm(forms.ModelForm):
    """ form para encargados de ruta"""
    class Meta:
        model = EncargadoRuta
        # campos que muestra el formulario
        fields = ("nombres", "ap_paterno", "ap_materno", "sexo", "telefono", \
        "domicilio", "email", "departamento")
        labels = {
            'ap_paterno': 'Apellido Paterno', 'ap_materno': 'Apellido Materno',
            'sexo': 'Género', 'email': 'Correo Electrónico', 'telefono': 'Teléfono'
        }
        
    def __init__(self, *args, **kwargs):
        """ método que itera los campos del form y agrega la clase form-control de bootstrap a los input"""
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
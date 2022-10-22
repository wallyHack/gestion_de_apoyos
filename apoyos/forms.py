
from django import forms
from .models import Localidad

class LocalidadesForm(forms.ModelForm):
    """ form para Localidades"""
    class Meta:
        model = Localidad
        #fields = '__all__'

        # campos que muestra el formulario
        fields = ("nombre", "seccion", "tipo")
        exclude = ['numero_habitantes']

    def __init__(self, *args, **kwargs):
        """ método que itera los campos del form y agrega la clase form-control de bootstrap a todos"""
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


from django import forms
from .models import Contribuyente

class ContribuyenteForm(forms.ModelForm):
    """ form de contribuyente"""
    class Meta:
        model = Contribuyente
        # campos que muestra el form
        fields = ("numero_de_cuenta_predial", "nombre", "ap_paterno", "ap_materno", "genero", "domicilio", "localidad", "telefono", "expediente", "notas_adicionales")
        # etiquetas
        labels = {
            "numero_de_cuenta_predial": "Número de cuenta predial", 
            "nombre": "Nombre",
            "ap_paterno": "Apellido Paterno",
            "ap_materno": "Apellido Materno",
            "genero": "Género",
            "localidad": "Localidad",
            "expediente": "Expediente",
            "notas_adicionales": "Notas Adicionales"
        }
        
    def __init__(self, *args, **kwargs):
        """ método que itera los campos del form y agrega la clase form-control de bootstrap a los input"""
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
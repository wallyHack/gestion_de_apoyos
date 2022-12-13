
from django import forms
from .models import Contribuyente
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class ContribuyenteForm(forms.ModelForm):
    """ form de contribuyente"""
    
    # validaciones en el lado del servidor
    numero_de_cuenta_predial = forms.IntegerField(min_value=1, required=True)
    nombre = forms.CharField(min_length=1, max_length=100, required=True)
    ap_paterno = forms.CharField(required=True)
    expediente = forms.FileField(required=False)
    localidad = forms.CharField(required=True)
    telefono = forms.IntegerField(required=True)
    
    # validamos que no haya registros duplicados con el mismo numero de predial
    # def clean_numero_de_cuenta_predial(self):
        # extraemos el valor que ingreso el usuario en el campo
        # numero_de_cuenta_predial = self.cleaned_data["numero_de_cuenta_predial"] 
        # existe = Contribuyente.objects.filter(numero_de_cuenta_predial=numero_de_cuenta_predial).exists()
        
        # if existe:
        #   raise ValidationError("Ya existe un contribuyentre con este numero de predial..")      
      
        # return numero_de_cuenta_predial

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
            
    def clean(self):
        try:
            sc = Contribuyente.objects.get(
                numero_de_cuenta_predial = self.cleaned_data['numero_de_cuenta_predial']
            )
            
            if not self.instance.pk:
                raise ValidationError("Ya existe un contribuyente con este numero de predial..")
            elif self.instance.pk != sc.pk:
                raise forms.ValidationError("Cambio no permitido, coincide con otro registro")
            
        except Contribuyente.DoesNotExist:
            pass            
        return self.cleaned_data
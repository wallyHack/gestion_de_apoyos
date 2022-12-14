
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from .models import Apoyos, Departamento, Localidad, Persona, EncargadoRuta, Puesto, Empleado

class LocalidadesForm(forms.ModelForm):
    """ form para Localidades"""
    # validaciones en el servidor
    nombre = forms.CharField(required=True)
    
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
    # validaciones en el servidor
    curp = forms.CharField(required=True)
    nombres = forms.CharField(required=True)
    ap_paterno = forms.CharField(required=True)
    
    class Meta:
        model = Persona
        # campos que muestra el formulario
        fields = ("curp", "nombres", "ap_paterno", "ap_materno", "tipo", "genero", \
        "fecha_de_nacimiento","domicilio", "estado", "telefono", "localidad")
        labels = {
            'curp': 'CURP', 'nombres': 'Nombres', 'ap_paterno': 'Apellido Paterno', \
            'ap_materno': 'Apellido Materno', 'genero': 'Género', 'fecha_de_nacimiento':'Fecha de Nacimiento'
        }
        
    def __init__(self, *args, **kwargs):
        """ método que itera los campos del form y agrega la clase form-control de bootstrap a los input"""
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
        # al select y/o combo box de localidades le agregamos un valor por defecto
        self.fields['localidad'].empty_label = 'Seleccione localidad..'  
        
    def clean(self):
        try:
            sc = Persona.objects.get(
                curp=self.cleaned_data['curp'].upper()
            )
            
            if not self.instance.pk:
                raise forms.ValidationError("Ya existe una persona con esta CURP..")
            elif self.instance.pk != sc.pk:
                raise forms.ValidationError("Cambio no permitido, coincide con otro registro..")
            
        except Persona.DoesNotExist:
            pass
        return self.cleaned_data          
            
class EncargadosRutaForm(forms.ModelForm):
    """ form para encargados de ruta"""
    class Meta:
        model = EncargadoRuta
        # campos que muestra el formulario
        fields = ("nombres", "ap_paterno", "ap_materno", "foto", "sexo", "telefono", \
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
            
        # al select y/o combo box de departamento le agregamos un valor por defecto
        self.fields['departamento'].empty_label = 'Seleccione departamento..'
        
class PuestosForm(forms.ModelForm):
    """ form para puestos"""
    # validaciones en el servidor
    nombre = forms.CharField(required=True)
    class Meta:
        model = Puesto
        # campos que muestra el form
        fields = ("__all__")
        labels = {
            'nombre': 'Nombre'
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
            sc = Puesto.objects.get(
                nombre=self.cleaned_data['nombre'].upper()
            )
            
            if not self.instance.pk:
                raise forms.ValidationError("Ya existe un puesto de trabajo con este nombre..")
            elif self.instance.pk != sc.pk:
                raise forms.ValidationError("Cambio no permitido, coincide con otro registro..")
        
        except Puesto.DoesNotExist:
            pass
        return self.cleaned_data
                    
class DepartamentoForm(forms.ModelForm):
    """ form para departamentos"""
    # validaciones en el servidor
    nombre = forms.CharField(required=True)
    titular = forms.CharField(required=True)
    
    class Meta:
        """Meta definition for DepartamentoForm"""
        model = Departamento        
        # campos que muestra el form
        fields = ('nombre', 'titular', 'telefono', 'email', 'numero_de_empleados')
        labels = {
            'nombre': 'Nombre',
            'titular': 'Titular',
            'telefono': 'Teléfono',
            'email': 'Correo Electrónico',
            'numero_de_empleados': 'Número de empleados'
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
            sc = Departamento.objects.get(
                nombre=self.cleaned_data['nombre'].upper()                
            )
            if not self.instance.pk:
                raise forms.ValidationError("Ya existe un departamento con este nombre..")
            elif self.instance.pk != sc.pk:
                raise forms.ValidationError("Cambio no permitido, coincide con otro registro..")
                
        except Departamento.DoesNotExist:
            pass
        return self.changed_data
            
class EmpleadosForm(forms.ModelForm):
    """ form para empleados"""
    # validaciones en el servidor
    nombre = forms.CharField(required=True)
    ap_paterno = forms.CharField(required=True)
 
    class Meta:
        """Meta definition for Empleadosform"""

        model = Empleado
        # campos que muestra el form
        fields = ('nombre', 'ap_paterno', 'ap_materno', 'tipo_de_empleado', 'domicilio', 'telefono',
        'genero', 'status', 'departamento', 'puesto', 'sueldo')
        labels = {
            'nombre': 'Nombre', 'ap_paterno': 'Apellido Paterno', 'tipo_de_empleado': 'Tipo', 'ap_materno': 'Apellido Materno',
            'domicilio': 'Domicilio', 'telefono':'Teléfono', 'genero': 'Genéro', 'status': 'Estatus',
            'departamento': 'Departamento', 'puesto': 'Puesto', 'sueldo': 'Sueldo'
        }
                
    def __init__(self, *args, **kwargs):
        """ método que itera los campos del form y agrega la clase form-control de bootstrap a los input"""
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
                                
        # al select y/o combo box de departamento y puesto le agregamos un valor por defecto
        self.fields['departamento'].empty_label = 'Seleccione un departamento..'
        self.fields['puesto'].empty_label = 'Seleccione un puesto..'
        
       

class ApoyosForm(forms.ModelForm):
    """form para apoyos"""

    class Meta:
        """Meta definition for ApoyosForm"""

        model = Apoyos
        fields = ('tipo', 'descripcion', 'fecha_de_entrega', 'foto_de_comprobacion', \
        'notas_adicionales', 'persona', 'encargado_de_ruta')
        labels = {
            'tipo': 'Tipo',
            'descripcion': 'Descripción',
            'fecha_de_entrega': 'Fecha de entrega',
            'foto_de_comprobacion': 'Imagen de comprobación',
            'notas_adicionales': 'Notas adicionales',
            'persona': 'Persona', 
            'encargado_de_ruta': 'Encargado de ruta'
        }
        
    def __init__(self, *args, **kwargs):
        """ método que itera los campos del form y agrega la clase form-control de bootstrap a los input"""
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
        self.fields['fecha_de_entrega'].widget.attrs['readonly'] = True  
            
        # al select y/o combo box de persona y puesto le agregamos un valor por defecto
        self.fields['persona'].empty_label = 'Seleccione la persona..'
        self.fields['encargado_de_ruta'].empty_label = 'Seleccione el encargado de ruta..'

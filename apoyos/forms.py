
from django import forms
from .models import Apoyos, Departamento, Localidad, Persona, EncargadoRuta, Puesto, Empleado

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
        fields = ("curp", "nombres", "ap_paterno", "ap_materno", "tipo", "genero", \
        "domicilio", "estado", "telefono", "localidad")
        labels = {
            'curp': 'CURP', 'nombres': 'Nombres', 'ap_paterno': 'Apellido Paterno', \
            'ap_materno': 'Apellido Materno', 'genero': 'Género'
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
            
        # al select y/o combo box de departamento le agregamos un valor por defecto
        self.fields['departamento'].empty_label = 'Seleccione departamento..'
        
class PuestosForm(forms.ModelForm):
    """ form para puestos"""
    
    class Meta:
        model = Puesto
        # campos que muestra el form
        fields = '__all__'
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
            
class DepartamentoForm(forms.ModelForm):
    """ form para departamentos"""

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
            
class EmpleadosForm(forms.ModelForm):
    """ form para empleados"""

    class Meta:
        """Meta definition for Empleadosform"""

        model = Empleado
        # campos que muestra el form
        fields = ('nombre', 'ap_paterno', 'ap_materno', 'tipo_de_empleado', 'domicilio', 'telefono',
        'genero', 'status', 'departamento', 'puesto', 'sueldo')
        labels = {
            'nombre': 'Nombre', 'ap_paterno': 'Apellido Paterno', 'tipo_de_empleado': 'Tipo', 'ap_materno': 'Apellido Materno',
            'domicilio': 'Domicilio', 'telefono':'Teléfono', 'genero': 'Genéro', 'status': 'Status',
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
        self.fields['tipo_de_empleado'].empty_label = 'Seleccione el tipo de empleado..'
        self.fields['departamento'].empty_label = 'Seleccione departamento..'
        self.fields['puesto'].empty_label = 'Seleccione el puesto..'

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
            
        # al select y/o combo box de persona y puesto le agregamos un valor por defecto
        self.fields['persona'].empty_label = 'Seleccione la persona..'
        self.fields['encargado_de_ruta'].empty_label = 'Seleccione el encargado de ruta..'

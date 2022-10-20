

from dataclasses import fields
from django import forms
from .models import Persona, Localidad

class LocalidadesForm(forms.ModelForm):
   """ form para Localidades"""
   class Meta:
       model = Localidad
       fields = '__all__'
       #fields = ("id", "nombre", "seccion", "numero_habitantes")

class PersonaForm(forms.ModelForm):
    """form para personas"""

    class Meta:
        """Meta definition for Personaform."""
        model = Persona
        fields = '__all__'
        #fields = ('nombres', 'ap_paterno', 'ap_materno', 'tipo', 'localidad', 'estado', 'telefono')

        
    

from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from bases.views import HomeSinPrivilegios 
from .forms import LocalidadesForm, PersonasForm, EncargadosRutaForm, PuestosForm
from.models import Localidad, Puesto, Persona, EncargadoRuta, Apoyos, Empleado, Departamento

# Create your views here.
class LocalidadView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase para listar localidades"""
    model = Localidad
    template_name = "apoyos/localidades_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class LocalidadNew(LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para llenar form de localidad"""
    model = Localidad
    template_name = "apoyos/localidades_form.html"
    context_object_name = "obj"
    form_class = LocalidadesForm
    success_url = reverse_lazy("apoyos:localidades_list")
    login_url = "bases:login"
    
class LocalidadEdit(LoginRequiredMixin, generic.UpdateView):
    """ vista basada en clase para editar form de localidad"""
    model = Localidad
    template_name = "apoyos/localidades_form.html"
    context_object_name = "obj"
    form_class = LocalidadesForm
    success_url = reverse_lazy("apoyos:localidades_list")
    login_url = "bases:login"
    
class LocalidadDelete(LoginRequiredMixin, generic.DeleteView):
    """ vista basada en clase para eliminar una localidad"""
    model = Localidad
    template_name = "apoyos/localidades_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("apoyos:localidades_list")
    
#*********************************************************************************

class PersonaView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase para listar personas"""
    model = Persona
    template_name = "apoyos/personas_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class PersonaNew(LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para agregar personas"""
    model = Persona
    template_name = "apoyos/personas_form.html"
    context_object_name = "obj"
    form_class = PersonasForm
    success_url = reverse_lazy("apoyos:personas_list")
    login_url = "bases:login"
    
class PersonaEdit(LoginRequiredMixin, generic.UpdateView):
    """ vista basada en clase para actualizar personas"""
    model = Persona
    template_name = "apoyos/personas_form.html"
    context_object_name = "obj"
    form_class = PersonasForm
    success_url = reverse_lazy("apoyos:personas_list")
    login_url = "bases:login"
    
class PersonaDelete(LoginRequiredMixin, generic.DeleteView):
    """ vista basada en clase para eliminar personas"""
    model = Persona
    template_name = "apoyos/personas_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("apoyos:personas_list")
    
#*********************************************************************************

class EncargadoRutaView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase para listar encargados de ruta"""
    model = EncargadoRuta
    template_name = "apoyos/encargados_ruta_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class EncargadoRutaNew(LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para agregar encargados de ruta"""
    model = EncargadoRuta
    template_name = "apoyos/encargados_ruta_form.html"
    context_object_name = "obj"
    form_class = EncargadosRutaForm
    success_url = reverse_lazy("apoyos:encargados_list")
    login_url = "bases:login"
    
class EncargadoRutaEdit(LoginRequiredMixin, generic.UpdateView):
    """ vista basada en clase para actualizar encargados de ruta"""
    model = EncargadoRuta
    template_name = "apoyos/encargados_ruta_form.html"
    context_object_name = "obj"
    form_class = EncargadosRutaForm
    success_url = reverse_lazy("apoyos:encargados_list")
    login_url = "bases:login"
    
class EncargadoRutaDelete(LoginRequiredMixin, generic.DeleteView):
    """ vista basada en clase para eliminar encargados de ruta"""
    model = EncargadoRuta
    template_name = "apoyos/encargados_ruta_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("apoyos:encargados_list")
    
#*********************************************************************************
    
class PuestoView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase para listar los puestos"""
    model = Puesto
    template_name = "apoyos/puestos_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class PuestoNew(LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para llenar form de puesto"""
    model = Puesto
    template_name = "apoyos/puestos_form.html"
    context_object_name = "obj"
    form_class = PuestosForm
    success_url = reverse_lazy("apoyos:puestos_list")
    login_url = "bases:login"
    
class PuestoEdit(LoginRequiredMixin, generic.UpdateView):
    """ vista basada en clase para editar form de puesto"""
    model = Puesto
    template_name = "apoyos/puestos_form.html"
    context_object_name = "obj"
    form_class = PuestosForm
    success_url = reverse_lazy("apoyos:puestos_list")
    login_url = "bases:login"
    
class PuestoDelete(LoginRequiredMixin, generic.DeleteView):
    """ vista basada en clase para eliminar un puesto"""
    model = Puesto
    template_name = "apoyos/puestos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("apoyos:puestos_list")
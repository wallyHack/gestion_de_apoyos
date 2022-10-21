from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from bases.views import HomeSinPrivilegios 
from .forms import LocalidadesForm, PersonaForm
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
    
class LocalidadDelete(SuccessMessageMixin, generic.edit.DeleteView):
    """ vista basada en clase para eliminar una localidad"""
    model = Localidad
    template_name = "apoyos/localidades_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("apoyos:localidades_list")
    
#*********************************************************************************
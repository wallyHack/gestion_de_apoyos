from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from bases.views import HomeSinPrivilegios 

from.models import Localidad, Puesto, Persona, EncargadoRuta, Apoyos, Empleado, Departamento

# Create your views here.
class PersonaView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase que lista los personas que son activistas/activados"""
    model = Persona
    template_name = "apoyos/personas_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
from django.shortcuts import render, redirect
from .models import Contribuyente
from bases.views import Sin_Privilegios
from django.views import generic
from .forms import ContribuyenteForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.
class ContribuyenteView(Sin_Privilegios, generic.ListView):
    """ vista basada en clase para listar localidades"""
    permission_required = "catastro.view_contribuyente"
    model = Contribuyente
    template_name = "catastro/contribuyentes_list.html"
    context_object_name = "obj" 
    
class ContribuyenteNew(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
    """ vista basada en clase para agregar contribuyentes"""
    permission_required = "catastro.add_contribuyente"
    model = Contribuyente
    template_name = "catastro/contribuyentes_form.html"
    context_object_name = "obj"
    form_class = ContribuyenteForm
    success_message = "Contribuyente agregado satisfactoriamente.."
    success_url = reverse_lazy("catastro:contribuyentes_list")
        
class ContribuyenteEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):
    """ vista basada en clase para actualizar contribuyentes"""
    permission_required = "catastro.change_contribuyente"
    model = Contribuyente
    template_name = "catastro/contribuyentes_form.html"
    context_object_name = "obj"
    form_class = ContribuyenteForm
    success_message = "Contribuyente actualizado satisfactoriamente.."
    success_url = reverse_lazy("catastro:contribuyentes_list")
    
class ContribuyenteDelete(SuccessMessageMixin, Sin_Privilegios, generic.DeleteView):
    """ vista basada en clase para eliminar contribuyentes"""
    permission_required = "catastro.delete_contribuyente"
    model = Contribuyente
    template_name = "catastro/contribuyentes_del.html"
    context_object_name = "obj"
    success_message = "Contribuyente eliminado satisfactoriamente.."
    success_url = reverse_lazy("catastro:contribuyentes_list")
    

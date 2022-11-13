
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from logging import raiseExceptions
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.contrib import messages
from apoyos.models import Persona
from django.shortcuts import render, redirect

# Create your views here.
class Sin_Privilegios(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'bases:login'
    raiseExceptions = False # no se ponga la pantalla en blanco
    redirect_field_name = "redirect_to"

    def handle_no_permission(self):
        """ método que valida si el usuario tiene privilegios, para redireccionar a plantilla"""
        from django.contrib.auth.models import AnonymousUser

        # si el usuario es válido, se muestra la vista sin privilegios
        if not self.request.user == AnonymousUser():
            self.login_url = "bases:sin_privilegios"

        return HttpResponseRedirect(reverse_lazy(self.login_url))
    
class Home(LoginRequiredMixin, TemplateView):    
    template_name = 'bases/home.html'
    login_url = 'bases:login' # sino esta logeado se redireccona al admin

class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = 'bases:login'
    template_name = "bases/sin_privilegios.html"
    
def getActivistas(request):
    """ mostrar todos los activistas"""
    activistas = Persona.objects.all().filter(tipo="ACTIVISTA").count()
    print(activistas)
    template_name = "apoyos/activistas.html"
    context = {'obj': activistas}
    
    return render(request, template_name, context)


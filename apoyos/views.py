from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from bases.views import HomeSinPrivilegios 
from .forms import ApoyosForm, DepartamentoForm, EmpleadosForm, LocalidadesForm, PersonasForm, EncargadosRutaForm, PuestosForm
from.models import Localidad, Puesto, Persona, EncargadoRuta, Apoyos, Empleado, Departamento

# Create your views here.
class LocalidadView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase para listar localidades"""
    model = Localidad
    template_name = "apoyos/localidades_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class LocalidadNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para llenar form de localidad"""
    model = Localidad
    template_name = "apoyos/localidades_form.html"
    context_object_name = "obj"
    form_class = LocalidadesForm    
    success_message = "Localidad agregada satisfactoriamente.."
    success_url = reverse_lazy("apoyos:localidades_list")
    login_url = "bases:login"
    
        
class LocalidadEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """ vista basada en clase para editar form de localidad"""
    model = Localidad
    template_name = "apoyos/localidades_form.html"
    context_object_name = "obj"
    form_class = LocalidadesForm    
    success_message = "Localidad actualizada satisfactoriamente.."
    success_url = reverse_lazy("apoyos:localidades_list")
    login_url = "bases:login"
    
    
class LocalidadDelete(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """ vista basada en clase para eliminar una localidad"""
    model = Localidad
    template_name = "apoyos/localidades_del.html"
    context_object_name = "obj"
    success_message = "Localidad eliminada satisfactoriamente.."
    success_url = reverse_lazy("apoyos:localidades_list")
    
#*********************************************************************************

class PersonaView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase para listar personas"""
    model = Persona
    template_name = "apoyos/personas_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class PersonaNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para agregar personas"""
    model = Persona
    template_name = "apoyos/personas_form.html"
    context_object_name = "obj"
    form_class = PersonasForm
    success_message = "Persona agregada satisfactoriamente.."
    success_url = reverse_lazy("apoyos:personas_list")
    login_url = "bases:login"
    
class PersonaEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """ vista basada en clase para actualizar personas"""
    model = Persona
    template_name = "apoyos/personas_form.html"
    context_object_name = "obj"
    form_class = PersonasForm
    success_message = "Persona actualizada satisfactoriamente.."
    success_url = reverse_lazy("apoyos:personas_list")
    login_url = "bases:login"
    
class PersonaDelete(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """ vista basada en clase para eliminar personas"""
    model = Persona
    template_name = "apoyos/personas_del.html"
    context_object_name = "obj"
    success_message = "Persona eliminada satisfactoriamente.."
    success_url = reverse_lazy("apoyos:personas_list")
    
#*********************************************************************************

class EncargadoRutaView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase para listar encargados de ruta"""
    model = EncargadoRuta
    template_name = "apoyos/encargados_ruta_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class EncargadoRutaNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para agregar encargados de ruta"""
    model = EncargadoRuta
    template_name = "apoyos/encargados_ruta_form.html"
    context_object_name = "obj"
    form_class = EncargadosRutaForm
    success_message = "Encargado de ruta agregado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:encargados_list")
    login_url = "bases:login"
    
class EncargadoRutaEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """ vista basada en clase para actualizar encargados de ruta"""
    model = EncargadoRuta
    template_name = "apoyos/encargados_ruta_form.html"
    context_object_name = "obj"
    form_class = EncargadosRutaForm
    success_message = "Encargado de ruta actualizado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:encargados_list")
    login_url = "bases:login"
    
class EncargadoRutaDelete(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """ vista basada en clase para eliminar encargados de ruta"""
    model = EncargadoRuta
    template_name = "apoyos/encargados_ruta_del.html"
    context_object_name = "obj"
    success_message = "Encargado de ruta eliminado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:encargados_list")
    
#*********************************************************************************
    
class PuestoView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase para listar los puestos"""
    model = Puesto
    template_name = "apoyos/puestos_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class PuestoNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para llenar form de puesto"""
    model = Puesto
    template_name = "apoyos/puestos_form.html"
    context_object_name = "obj"
    form_class = PuestosForm
    success_message = "Puesto agregado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:puestos_list")
    login_url = "bases:login"
    
class PuestoEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """ vista basada en clase para editar form de puesto"""
    model = Puesto
    template_name = "apoyos/puestos_form.html"
    context_object_name = "obj"
    form_class = PuestosForm
    success_message = "Puesto actualizado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:puestos_list")
    login_url = "bases:login"
    
class PuestoDelete(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """ vista basada en clase para eliminar un puesto"""
    model = Puesto
    template_name = "apoyos/puestos_del.html"
    context_object_name = "obj"
    success_message = "Puesto eliminado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:puestos_list")
    
#*********************************************************************************

class DepartamentoView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase para listar los departamentos"""
    model = Departamento
    template_name = "apoyos/departamentos_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class DepartamentoNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para llenar form de departamento"""
    model = Departamento
    template_name = "apoyos/departamentos_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_message = "Departamento agregado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:departamentos_list")
    login_url = "bases:login"
    
class DepartamentoEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """ vista basada en clase para editar form de departamento"""
    model = Departamento
    template_name = "apoyos/departamentos_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_message = "Departamento actualizado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:departamentos_list")
    login_url = "bases:login"

class DepartamentoDelete(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """ vista basada en clase para eliminar un departamento"""
    model = Departamento
    template_name = "apoyos/departamentos_del.html"
    context_object_name = "obj"
    success_message = "Departamento eliminado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:departamentos_list")
    
#*********************************************************************************

class EmpleadoView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase para listar los empleados"""
    model = Empleado
    template_name = "apoyos/empleados_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class EmpleadoNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para llenar form de empleado"""
    model = Empleado
    template_name = "apoyos/empleados_form.html"
    context_object_name = "obj"
    form_class = EmpleadosForm
    success_message = "Empleado agregado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:empleados_list")
    login_url = "bases:login"
    
class EmpleadoEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """ vista basada en clase para editar form de empleado"""
    model = Empleado
    template_name = "apoyos/empleados_form.html"
    context_object_name = "obj"
    form_class = EmpleadosForm
    success_message = "Empleado actualizado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:empleados_list")
    login_url = "bases:login"
    
class EmpleadoDelete(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """ vista basada en clase para eliminar un empleado"""
    model = Empleado
    template_name = "apoyos/empleados_del.html"
    context_object_name = "obj"
    success_message = "Empleado eliminado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:empleados_list")
    
#*********************************************************************************

class ApoyosView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase para listar los apoyos"""
    model = Apoyos
    template_name = "apoyos/apoyos_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class ApoyosNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para llenar form de apoyo"""
    model = Apoyos
    template_name = "apoyos/apoyos_form.html"
    context_object_name = "obj"
    form_class = ApoyosForm
    success_message = "Apoyo agregado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:apoyos_list")
    login_url = "bases:login"
    
class ApoyosEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """ vista basada en clase para editar form de apoyos"""
    model = Apoyos
    template_name = "apoyos/apoyos_form.html"
    context_object_name = "obj"
    form_class = ApoyosForm
    success_message = "Apoyo actualizado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:apoyos_edit")
    login_url = "bases:login"
    
class ApoyosDelete(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """ vista basada en clase para eliminar un apoyo"""
    model = Apoyos
    template_name = "apoyos/apoyos_del.html"
    context_object_name = "obj"
    success_message = "Apoyo eliminado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:apoyos_list")
    
#*********************************************************************************
# filtros personalizados 
def comunidades_por_encargado(request, id):
    """ mostrar todas las comunidades que administra un encargado de ruta"""
    encargado = EncargadoRuta.objects.prefetch_related('comunidades').filter(pk=id)
    nombre_de_encargado = ""
    comunidades = {}
    for e in encargado:
        nombre_de_encargado = e.nombres +' '+ e.ap_paterno +' '+ e.ap_materno
        comunidades = e.comunidades.all()
        
    comunidadaes = list(comunidades)
    print(nombre_de_encargado)
    print(list(comunidades))
    # print(comunidades)
    # print(type(encargado))
    # encargado = list(encargado)    
    # print(type(encargado))
    #for e in encargado:
        #print(e.nombres, e.comunidades.all())        
    context = {'obj': comunidades, 'nombre_de_encargado': nombre_de_encargado}
    template_name = "apoyos/comunidades-er.html"
    
    # if not encargado:
    #     return redirect('apoyos:encargados_list')
    
    return render(request, template_name, context)
    
def apoyos_por_persona(request, id):
    """ mostramos todos los apoyos que ha recibido una persona"""
    apoyos_recibidos = Apoyos.objects.all().select_related('persona').filter(persona=id)
    print(apoyos_recibidos)

    context = {'obj': apoyos_recibidos}
    template_name = "apoyos/apoyos_recibidos.html"
    
    # if not apoyos_recibidos:
    #     return redirect('apoyos:apoyos_list')

    return render(request, template_name, context)



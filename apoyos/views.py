from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ApoyosForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from bases.views import Sin_Privilegios 
from .forms import ApoyosForm, DepartamentoForm, EmpleadosForm, LocalidadesForm, PersonasForm, EncargadosRutaForm, PuestosForm
from.models import Localidad, Puesto, Persona, EncargadoRuta, Apoyos, Empleado, Departamento

# Create your views here.
class LocalidadView(Sin_Privilegios, generic.ListView):
    """ vista basada en clase para listar localidades"""
    permission_required = "apoyos.view_localidad"
    model = Localidad
    template_name = "apoyos/localidades_list.html"
    context_object_name = "obj" 
    
class LocalidadNew(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
    """ vista basada en clase para llenar form de localidad"""
    permission_required = "apoyos.add_localidad"
    model = Localidad
    template_name = "apoyos/localidades_form.html"
    context_object_name = "obj"
    form_class = LocalidadesForm    
    success_message = "Localidad agregada satisfactoriamente.."
    success_url = reverse_lazy("apoyos:localidades_list") 
        
class LocalidadEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):
    """ vista basada en clase para editar form de localidad"""
    permission_required = "apoyos.change_localidad"
    model = Localidad
    template_name = "apoyos/localidades_form.html"
    context_object_name = "obj"
    form_class = LocalidadesForm    
    success_message = "Localidad actualizada satisfactoriamente.."
    success_url = reverse_lazy("apoyos:localidades_list")        
    
class LocalidadDelete(SuccessMessageMixin, Sin_Privilegios, generic.DeleteView):
    """ vista basada en clase para eliminar una localidad"""
    permission_required = "apoyos.delete_localidad"
    model = Localidad
    template_name = "apoyos/localidades_del.html"
    context_object_name = "obj"
    success_message = "Localidad eliminada satisfactoriamente.."
    success_url = reverse_lazy("apoyos:localidades_list")
    
#*********************************************************************************

class PersonaView(Sin_Privilegios, generic.ListView):
    """ vista basada en clase para listar personas"""
    permission_required = "apoyos.view_persona"
    model = Persona
    template_name = "apoyos/personas_list.html"
    context_object_name = "obj"
    
class PersonaNew(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
    """ vista basada en clase para agregar personas"""
    permission_required = "apoyos.add_persona"
    model = Persona
    template_name = "apoyos/personas_form.html"
    context_object_name = "obj"
    form_class = PersonasForm
    success_message = "Persona agregada satisfactoriamente.."
    success_url = reverse_lazy("apoyos:personas_list")   
    
class PersonaEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):
    """ vista basada en clase para actualizar personas"""
    permission_required = "apoyos.change_persona"
    model = Persona
    template_name = "apoyos/personas_form.html"
    context_object_name = "obj"
    form_class = PersonasForm
    success_message = "Persona actualizada satisfactoriamente.."
    success_url = reverse_lazy("apoyos:personas_list")    
    
class PersonaDelete(SuccessMessageMixin, Sin_Privilegios, generic.DeleteView):
    """ vista basada en clase para eliminar personas"""
    permission_required = "apoyos.delete_persona"
    model = Persona
    template_name = "apoyos/personas_del.html"
    context_object_name = "obj"
    success_message = "Persona eliminada satisfactoriamente.."
    success_url = reverse_lazy("apoyos:personas_list")
    
#*********************************************************************************

class EncargadoRutaView(Sin_Privilegios, generic.ListView):
    """ vista basada en clase para listar encargados de ruta"""
    permission_required = "apoyos.view_encargadoruta"
    model = EncargadoRuta
    template_name = "apoyos/encargados_ruta_list.html"
    context_object_name = "obj"
    
class EncargadoRutaNew(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
    """ vista basada en clase para agregar encargados de ruta"""
    permission_required = "apoyos.add_encargadoruta"
    model = EncargadoRuta
    template_name = "apoyos/encargados_ruta_form.html"
    context_object_name = "obj"
    form_class = EncargadosRutaForm
    success_message = "Encargado de ruta agregado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:encargados_list")    
    
class EncargadoRutaEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):
    """ vista basada en clase para actualizar encargados de ruta"""
    permission_required = "apoyos.change_encargadoruta"
    model = EncargadoRuta
    template_name = "apoyos/encargados_ruta_form.html"
    context_object_name = "obj"
    form_class = EncargadosRutaForm
    success_message = "Encargado de ruta actualizado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:encargados_list")    
    
class EncargadoRutaDelete(SuccessMessageMixin, Sin_Privilegios, generic.DeleteView):
    """ vista basada en clase para eliminar encargados de ruta"""
    permission_required = "apoyos.delete_encargadoruta"
    model = EncargadoRuta
    template_name = "apoyos/encargados_ruta_del.html"
    context_object_name = "obj"
    success_message = "Encargado de ruta eliminado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:encargados_list")
    
#*********************************************************************************
    
class PuestoView(Sin_Privilegios, generic.ListView):
    """ vista basada en clase para listar los puestos"""
    permission_required = "apoyos.view_puesto"
    model = Puesto
    template_name = "apoyos/puestos_list.html"
    context_object_name = "obj"    
    
class PuestoNew(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
    """ vista basada en clase para llenar form de puesto"""
    permission_required = "apoyos.add_puesto"
    model = Puesto
    template_name = "apoyos/puestos_form.html"
    context_object_name = "obj"
    form_class = PuestosForm
    success_message = "Puesto agregado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:puestos_list")   
    
class PuestoEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):
    """ vista basada en clase para editar form de puesto"""
    permission_required = "apoyos.change_puesto"
    model = Puesto
    template_name = "apoyos/puestos_form.html"
    context_object_name = "obj"
    form_class = PuestosForm
    success_message = "Puesto actualizado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:puestos_list")    
    
class PuestoDelete(SuccessMessageMixin, Sin_Privilegios, generic.DeleteView):
    """ vista basada en clase para eliminar un puesto"""
    permission_required = "apoyos.delete_puesto"
    model = Puesto
    template_name = "apoyos/puestos_del.html"
    context_object_name = "obj"
    success_message = "Puesto eliminado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:puestos_list")
    
#*********************************************************************************

class DepartamentoView(Sin_Privilegios, generic.ListView):
    """ vista basada en clase para listar los departamentos"""
    permission_required = "apoyos.view_departamento"
    model = Departamento
    template_name = "apoyos/departamentos_list.html"
    context_object_name = "obj"    
    
class DepartamentoNew(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
    """ vista basada en clase para llenar form de departamento"""
    permission_required = "apoyos.add_departamento"
    model = Departamento
    template_name = "apoyos/departamentos_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_message = "Departamento agregado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:departamentos_list")    
    
class DepartamentoEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):
    """ vista basada en clase para editar form de departamento"""
    permission_required = "apoyos.change_departamento"
    model = Departamento
    template_name = "apoyos/departamentos_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_message = "Departamento actualizado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:departamentos_list")    

class DepartamentoDelete(SuccessMessageMixin, Sin_Privilegios, generic.DeleteView):
    """ vista basada en clase para eliminar un departamento"""
    permission_required = "apoyos.delete_departamento"
    model = Departamento
    template_name = "apoyos/departamentos_del.html"
    context_object_name = "obj"
    success_message = "Departamento eliminado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:departamentos_list")
    
#*********************************************************************************

class EmpleadoView(Sin_Privilegios, generic.ListView):
    """ vista basada en clase para listar los empleados"""
    permission_required = "apoyos.view_empleado"
    model = Empleado
    template_name = "apoyos/empleados_list.html"
    context_object_name = "obj"    
    
class EmpleadoNew(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
    """ vista basada en clase para llenar form de empleado"""
    permission_required = "apoyos.add_empleado"
    model = Empleado
    template_name = "apoyos/empleados_form.html"
    context_object_name = "obj"
    form_class = EmpleadosForm
    success_message = "Empleado agregado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:empleados_list")   
    
class EmpleadoEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):
    """ vista basada en clase para editar form de empleado"""
    permission_required = "apoyos.change_empleado"
    model = Empleado
    template_name = "apoyos/empleados_form.html"
    context_object_name = "obj"
    form_class = EmpleadosForm
    success_message = "Empleado actualizado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:empleados_list")    
    
class EmpleadoDelete(SuccessMessageMixin, Sin_Privilegios, generic.DeleteView):
    """ vista basada en clase para eliminar un empleado"""
    permission_required = "apoyos.delete_empleado"
    model = Empleado
    template_name = "apoyos/empleados_del.html"
    context_object_name = "obj"
    success_message = "Empleado eliminado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:empleados_list")
    
#*********************************************************************************

class ApoyosView(Sin_Privilegios, generic.ListView):
    """ vista basada en clase para listar los apoyos"""
    permission_required = "apoyos.view_apoyos"
    model = Apoyos
    template_name = "apoyos/apoyos_list.html"
    context_object_name = "obj"    
    
class ApoyosNew(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
    """ vista basada en clase para llenar form de apoyo"""
    permission_required = "apoyos.add_apoyos"
    model = Apoyos
    template_name = "apoyos/apoyos_form.html"
    context_object_name = "obj"
    form_class = ApoyosForm
    success_message = "Apoyo agregado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:apoyos_list")    
    
class ApoyosEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):
    """ vista basada en clase para editar form de apoyos"""
    permission_required = "apoyos.change_apoyos"
    model = Apoyos
    template_name = "apoyos/apoyos_form.html"
    context_object_name = "obj"
    form_class = ApoyosForm
    success_message = "Apoyo actualizado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:apoyos_list")
    
class ApoyosDelete(SuccessMessageMixin, Sin_Privilegios, generic.DeleteView):
    """ vista basada en clase para eliminar un apoyo"""
    permission_required = "apoyos.delete_apoyos"
    model = Apoyos
    template_name = "apoyos/apoyos_del.html"
    context_object_name = "obj"
    success_message = "Apoyo eliminado satisfactoriamente.."
    success_url = reverse_lazy("apoyos:apoyos_list")
    
#*********************************************************************************
# filtros personalizados 
@login_required(login_url='/login/') # debe estar logeado
@permission_required('apoyos.view_persona', login_url='bases:sin_privilegios')
def personas_por_comunidad(request, id):
    """ mostramos todas las personas de cada comunidad"""
    personas = Persona.objects.all().select_related('localidad').filter(localidad=id)
    #print(personas)
    
    template_name = 'apoyos/personas_por_comunidad.html'
    context = {'obj': personas}
    
    return render(request, template_name, context)

@login_required(login_url='/login/')
@permission_required('apoyos.view_empleado', login_url='bases:sin_privilegios')
def empleados_por_departamento(request, id):
    """ mostramos todos los empleados de cada departamento"""
    empleados = Empleado.objects.all().select_related('departamento').filter(departamento=id)
    #print(empleados)
    
    template_name = 'apoyos/empleados_por_departamento.html'
    context = {'obj': empleados}
    
    return render(request, template_name, context)

def empleados_por_puesto(request, id):
    """ mostramos todos los empleados de cada puesto"""
    empleados = Empleado.objects.all().select_related('puesto').filter(puesto=id);
    
    template_name = 'apoyos/empleados_por_puesto.html'
    context = {
        'obj': empleados
    }
    
    return render(request, template_name, context)

@login_required(login_url='/login/') # debe estar logeado
@permission_required('apoyos.view_apoyos', login_url='bases:sin_privilegios')
def apoyos_por_persona(request, id):
    """ mostramos todos los apoyos que ha recibido una persona"""
    apoyos_recibidos = Apoyos.objects.all().select_related('persona').filter(persona=id)
    #print(apoyos_recibidos)

    context = {'obj': apoyos_recibidos}
    template_name = "apoyos/apoyos_recibidos.html"
    
    return render(request, template_name, context)

@login_required(login_url='/login/') # debe estar logeado
@permission_required('apoyos.view_localidad', login_url='bases:sin_privilegios')
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

@login_required(login_url='/login/')
@permission_required('apoyos.view_persona', login_url='bases:sin_privilegios')
def getActivistas(request):
    """ mostrar todos los activistas"""
    activistas = Persona.objects.all().filter(tipo="ACTIVISTA")
    template_name = "apoyos/activistas.html"
    context = {'obj': activistas}
    
    return render(request, template_name, context)

@login_required(login_url='/login/')
@permission_required('apoyos.view_persona', login_url='bases:sin_privilegios')
def getActivados(request):
    """ mostrar todos los activados"""
    activados = Persona.objects.all().filter(tipo="ACTIVADO")
    
    template_name = "apoyos/activados.html"
    context = {'obj': activados}
    
    return render(request, template_name, context)

def agregarApoyos(request, nombre):
    """ agregamos un apoyo"""
    
    # form vacio
    data = {
        'form': ApoyosForm({
            'tipo': 'VIVIENDA',
            'descripcion': '1 carretilla', 
            'notas_adicionales': 'se entrego esto',
            'persona':nombre       
        })
    }
    
    if request.method == 'POST':
        formulario = ApoyosForm(data=request.POST or None, files=request.FILES)
        if formulario.is_valid():            
            formulario.save()
            messages.success(request, 'Agregado correctamente.')
            return redirect('apoyos:apoyos_list')
        else:
            data['form'] = formulario
    
    return render(request, 'apoyos/agregar-apoyo.html', data)
    
    




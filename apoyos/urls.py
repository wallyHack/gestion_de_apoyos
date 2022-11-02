
from django.urls import path
from .views import ApoyosView, LocalidadView, LocalidadNew, LocalidadEdit, LocalidadDelete, \
    PersonaView, PersonaNew, PersonaEdit, PersonaDelete, personas_por_comunidad, \
    EncargadoRutaView, EncargadoRutaNew, EncargadoRutaEdit, EncargadoRutaDelete, comunidades_por_encargado, \
    PuestoView, PuestoNew, PuestoEdit, PuestoDelete, \
    DepartamentoView, DepartamentoNew, DepartamentoEdit, DepartamentoDelete, \
    EmpleadoView, EmpleadoNew, EmpleadoEdit, EmpleadoDelete, empleados_por_departamento, \
    ApoyosView, ApoyosNew, ApoyosEdit, ApoyosDelete, apoyos_por_persona

urlpatterns = [
    # crud localidades
    path('localidades/', LocalidadView.as_view(), name='localidades_list'),
    path('localidades/new', LocalidadNew.as_view(), name='localidades_new'),
    path('localidades/edit/<int:pk>', LocalidadEdit.as_view(), name='localidades_edit'),
    path('localidades/delete/<int:pk>', LocalidadDelete.as_view(), name='localidades_delete'),
    
    # crud personas
    path('personas/', PersonaView.as_view(), name='personas_list'),
    path('personas/new', PersonaNew.as_view(), name='personas_new'),
    path('personas/edit/<int:pk>', PersonaEdit.as_view(), name='personas_edit'),
    path('personas/delete/<int:pk>', PersonaDelete.as_view(), name="personas_delete"),
    
    # personas de cada comunidad
    path('personas/personas-por-comunidad/<int:id>', personas_por_comunidad, name='personas_por_comunidad'),
    
    # crud de encargados de ruta
    path('encargados-ruta/', EncargadoRutaView.as_view(), name='encargados_list'),
    path('encargados-ruta/new', EncargadoRutaNew.as_view(), name='encargados_new'),
    path('encargados-ruta/edit/<int:pk>', EncargadoRutaEdit.as_view(), name='encargados_edit'),
    path('encargados-ruta/delete/<int:pk>', EncargadoRutaDelete.as_view(), name="encargados_delete"),
    
    # comunidadaes que dirige cada encargado de ruta
    path('encargados-ruta/comunidades-er/<int:id>', comunidades_por_encargado, name='comunidades-er'),    
    
    # crud de puestos
    path('puestos/', PuestoView.as_view(), name='puestos_list'),
    path('puestos/new', PuestoNew.as_view(), name='puestos_new'),
    path('puestos/edit/<int:pk>', PuestoEdit.as_view(), name='puestos_edit'),
    path('puestos/delete/<int:pk>', PuestoDelete.as_view(), name='puestos_delete'),
    
    # crud de departamentos
    path('departamentos/', DepartamentoView.as_view(), name='departamentos_list'),
    path('departamentos/new', DepartamentoNew.as_view(), name='departamentos_new'),
    path('departamentos/edit/<int:pk>', DepartamentoEdit.as_view(), name='departamentos_edit'),
    path('departamentos/delete/<int:pk>', DepartamentoDelete.as_view(), name='departamentos_delete'),
    
    # crud de empleados
    path('empleados/', EmpleadoView.as_view(), name='empleados_list'),
    path('empleados/new', EmpleadoNew.as_view(), name='empleados_new'),
    path('empleados/edit/<int:pk>', EmpleadoEdit.as_view(), name='empleados_edit'),
    path('empleados/delete/<int:pk>', EmpleadoDelete.as_view(), name='empleados_delete'),
    
    # empleados de cada departamento
    path('empleados/empleados-por-departamento/<int:id>', empleados_por_departamento, name='empleados_por_departamento'),
    
    # crud de apoyos
    path('apoyos/', ApoyosView.as_view(), name='apoyos_list'),
    path('apoyos/new', ApoyosNew.as_view(), name='apoyos_new'),
    path('apoyos/edit/<int:pk>', ApoyosEdit.as_view(), name='apoyos_edit'),
    path('apoyos/delete/<int:pk>', ApoyosDelete.as_view(), name='apoyos_delete'),
    
    # apoyos que ha recibido cada persona
    path('apoyos/apoyos-recibidos/<int:id>', apoyos_por_persona, name='apoyos-recibidos'),
]
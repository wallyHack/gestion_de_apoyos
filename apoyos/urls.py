
from django.urls import path
from .views import LocalidadView, LocalidadNew, LocalidadEdit, LocalidadDelete, \
    PersonaView, PersonaNew, PersonaEdit, PersonaDelete, \
    EncargadoRutaView, EncargadoRutaNew, EncargadoRutaEdit, EncargadoRutaDelete, \
    PuestoView, PuestoNew, PuestoEdit, PuestoDelete, \
    DepartamentoView, DepartamentoNew, DepartamentoEdit, DepartamentoDelete

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
    
    # crud de encargados de ruta
    path('encargados-ruta/', EncargadoRutaView.as_view(), name='encargados_list'),
    path('encargados-ruta/new', EncargadoRutaNew.as_view(), name='encargados_new'),
    path('encargados-ruta/edit/<int:pk>', EncargadoRutaEdit.as_view(), name='encargados_edit'),
    path('encargados-ruta/delete/<int:pk>', EncargadoRutaDelete.as_view(), name="encargados_delete"),
    
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
]
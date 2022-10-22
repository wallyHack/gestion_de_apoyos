
from django.urls import path
from .views import LocalidadView, LocalidadNew, LocalidadEdit, LocalidadDelete, PersonaView, \
    PersonaNew, PersonaEdit, PersonaDelete

urlpatterns = [
    # crud localidades
    path('localidades/', LocalidadView.as_view(), name='localidades_list'),
    path('localidades/new', LocalidadNew.as_view(), name='localidades_new'),
    path('localidades/edit/<int:pk>', LocalidadEdit.as_view(), name='localidades_edit'),
    path('categorias/delete/<int:pk>', LocalidadDelete.as_view(), name='localidades_delete'),
    
    # crud personas
    path('personas/', PersonaView.as_view(), name='personas_list'),
    path('personas/new', PersonaNew.as_view(), name='personas_new'),
    path('personas/edit/<int:pk>', PersonaEdit.as_view(), name='personas_edit'),
    path('personas/delete/<int:pk>', PersonaDelete.as_view(), name="personas_delete"),
]
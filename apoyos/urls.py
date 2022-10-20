
from django.urls import path
from .views import PersonaView, PersonaNew, LocalidadView, LocalidadNew

urlpatterns = [
    # crud localidades
    path('localidades/', LocalidadView.as_view(), name='localidades_list'),
    path('localidades/new', LocalidadNew.as_view(), name='localidades_new'),
    
    path('personas/', PersonaView.as_view(), name='persona_list'),
    path('personas/new', PersonaNew.as_view(), name='persona_new'),
    # path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    # path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    # path('categorias/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_del'),

]
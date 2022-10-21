
from django.urls import path
from .views import LocalidadView, LocalidadNew, LocalidadEdit, LocalidadDelete

urlpatterns = [
    # crud localidades
    path('localidades/', LocalidadView.as_view(), name='localidades_list'),
    path('localidades/new', LocalidadNew.as_view(), name='localidades_new'),
    path('localidades/edit/<int:pk>', LocalidadEdit.as_view(), name='localidades_edit'),
    path('categorias/delete/<int:pk>', LocalidadDelete.as_view(), name='localidades_delete'),
]
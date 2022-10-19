
from django.urls import path
from .views import PersonaView

urlpatterns = [
    path('personas/', PersonaView.as_view(), name='personas_list'),
    # path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    # path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    # path('categorias/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_del'),

]
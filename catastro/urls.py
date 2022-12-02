
from django.urls import path
from .views import ContribuyenteView, ContribuyenteNew, ContribuyenteEdit, ContribuyenteDelete

urlpatterns = [
    # crud de contribuyentes
    path('contribuyentes/', ContribuyenteView.as_view(), name='contribuyentes_list'),
    path('contribuyentes/new', ContribuyenteNew.as_view(), name='contribuyentes_new'),
    path('contribuyentes/edit/<int:pk>', ContribuyenteEdit.as_view(), name='contribuyentes_edit'),
    path('contribuyentes/delete/<int:pk>', ContribuyenteDelete.as_view(), name='contribuyentes_delete'),
]
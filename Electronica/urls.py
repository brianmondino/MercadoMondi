from django.shortcuts import render

# Create your views here.
from django.urls import path

from Electronica.views import Lista_Elec, Agregar, Buscar, Detalle_Elec, Borrar, Actualizar

urlpatterns =[
    path('', Lista_Elec.as_view(), name = 'Lista_Elec'),

        path('agregar/', Agregar.as_view(), name = 'agregar'),
        path('buscar/', Buscar, name = 'buscar'),
        path('detalle/<int:pk>/', Detalle_Elec.as_view(), name = 'detalles'),
        path('borrar/<int:pk>/', Borrar.as_view(), name = 'borrar'),
        path('actualizar/<int:pk>/', Actualizar.as_view(), name = 'actualizar'),
    ]
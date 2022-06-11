from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from Electronica.models import Electronics

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class Lista_Elec(ListView):
    modelo = Electronics
    template_name= 'Electronica_tem/elec_elec.html'
    queryset = Electronics.objects.filter(hay_stock = True)

class Detalle_Elec(DetailView):
    modelo = Electronics
    template_name= 'Electronica_tem/detalle_elec.html'

class Agregar(LoginRequiredMixin, CreateView):
    modelo = Electronics
    template_name = 'Electronica_tem/agregar_elec.html'
    campo = '__all__'

    def get_success_url(self):
        return reverse('Detalle_Elec', kwargs={'pk':self.object.pk})

class Borrar(DeleteView):
    model = Electronics
    template_name = 'Electronica_tem/borrar_elec.html'

    def get_success_url(self):
        return reverse('Lista_Elec')

class Actualizar(UpdateView):
    model = Electronics
    template_name = 'Electronica_tem/actualizar_elec.html'
    campo = '__all__'


    def get_success_url(self):
        return reverse('Detalle_Elec', kwargs = {'pk':self.object.pk})

def buscar(request):
    producto = Electronics.objects.filter(nombre__icontains=request.GET['buscar'])
    
    if producto.exists():
        context = {'producto':producto}
    else:
        context = {'errors':'No se encontro el producto'}

    return render(request, 'Electronica_tem/buscar_elec.html', context = context)
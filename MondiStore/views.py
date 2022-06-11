from django.contrib import admin
from django.urls import path, include

from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from MondiStore.forms import form_de_registracion

def index(request):
    print(request.user)
    print(request.user.is_authenticated)
    return render(request, 'index.html')

def registrarse(request):
    if request.method == 'POST':
        form = form_de_registracion(request.POST)

        if form.is_valid():
            form.save() #<------------propio del form
            usuario = form.cleaned_data['username']
            contrase = form.cleaned_data['password1']
            user = authenticate(username = usuario, password = contrase) #<----se llama asi para probar con otra variable
            login(request, user)
            context = {'message':f'Usuario creado correctamente, bienvenido {usuario}'}
            return render(request, 'index.html', context = context)
        else:
            errors = form.errors
            form = form_de_registracion()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth_tem/registrarse.html', context = context)
    else:
        form = form_de_registracion()
        context = {'form':form}
        return render(request, 'auth_tem/registrarse.html', context =context)


def loguearse(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data['username']  #<---- Acá va username siempre porque el AuthenticationForm usa estos campos
            contrase = form.cleaned_data['password'] #<---- Acá va password siempre
            user = authenticate(username=usuario, password=contrase)
            login(request, user)                                #<---------esto estaba dentro del if
            context = {'message':f'Bienvenido {usuario}!! :D'}  #<---------esto estaba dentro del if
            return render(request, 'index.html', context = context)  #<---------esto estaba dentro del if
            # if user is not None: # Pregunta EL USUARIO EXISTE?
            #     login(request, user)
            #     context = {'message':f'Bienvenido {usuario}!! :D'}
            #     return render(request, 'index.html', context = context)
            # else:
            #     context = {'errors':'No hay ningun usuario con esas credenciales!!!'}
            #     form = AuthenticationForm()
            #     return render(request, 'auth_tem/loguearse.html', context = context)
        else:
            errors = form.errors  #Guarda en la variable errors los errores del form AuthenticationForm
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form} 
            return render(request, 'auth_tem/loguearse.html', context = context)

    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth_tem/loguearse.html', context = context)


def desconectarse(request):
    logout(request)
    return redirect('index')

# def index(request):
#     print(request.user) # ?????????????????????????????????????
#     print(request.user.is_authenticated) # ?????????????????????????????????????
#     return render(request, 'index.html')


# def contacto(request):
#     if request.usuario.is_authenticated and request.usuario.is_superuser:
#         print(request.usuario.username)
#         return render(request, 'contacto.html')
#     else:
#         return redirect('login')

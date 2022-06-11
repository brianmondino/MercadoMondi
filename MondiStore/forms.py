from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class form_de_registracion(UserCreationForm):
    correo = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'correo', 'password1', 'password2'] #<----- aca username si o si ?
        help_texts = {sin_ayuda:'' for sin_ayuda in fields}
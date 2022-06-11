from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class form_de_registracion(UserCreationForm):
    correo = forms.EmailField()
    contrase1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    contrase2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

    class Meta:
        modelo = User
        campos = ['usuario', 'correo', 'contrase1', 'contrase2']
        help_texts = {sin_ayuda:'' for sin_ayuda in campos}
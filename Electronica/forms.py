
from django import forms
from Electronica.models import Electronics

class Electronics_form(forms.ModelForm):
    class Meta:
        model = Electronics
        fields = '__all__'

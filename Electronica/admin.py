from django.contrib import admin

# Register your models here.
from Electronica.models import Electronics

@admin.register(Electronics)
class Electronica_admin(admin.ModelAdmin):
    mostrar_display = ['nombre', 'precio', 'SKU', 'hay_stock']



from django.db import models

class Electronics(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    detalle = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    hay_stock = models.BooleanField(default=True)

    class Meta:
       verbose_name = 'Electronica'     #Estoy diciendo que cuando hable de 1 unidad lo llame asi
       verbose_name_plural = 'Electronicas' #Estoy diciendo que cuando hable de X unidades lo llame asi



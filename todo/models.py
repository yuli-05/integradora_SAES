from turtle import mode
from django.db import models



# Create your models here.

class ListMedicamentos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    cantidad = models.IntegerField(blank=False, null=False)
    fecha = models.DateField('fecha de caducidad', blank=False, null=False)

    def __str__(self):
        return self.nombre
from turtle import mode
from django.db import models



# Create your models here.

#Modelo de la lista de medicamentos

class ListMedicamentos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    cantidad = models.IntegerField(blank=False, null=False)
    fecha = models.DateField('fecha de caducidad', blank=False, null=False)

    def __str__(self):
        return self.nombre

#Modelo de la nota de evolucion
class NotaDeEvolucion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('fecha', blank=False, null=False)
    carrera = models.CharField(max_length=100, blank=False, null=False)
    grupo = models.IntegerField(blank=False, null=False)
    matricula = models.IntegerField(blank=False, null=False)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    edad = models.PositiveIntegerField(blank=False, null=False)
    sexo = models.CharField(max_length=15, blank=False, null=False)
    direccion = models.CharField(max_length=200, blank=False, null=False)
    peso = models.FloatField(blank=False, null=False)
    talla = models.FloatField(blank=False, null=False)
    presion = models.FloatField(blank=False, null=False)
    temperatura = models.FloatField(blank=False, null=False)
    padecimiento_actual  = models.CharField(max_length=100)
    alegias= models.CharField(max_length=2)
    cuales_alegias = models.CharField(max_length=100, )
    exploracion_fisica = models.CharField(max_length=100)
    otro = models.CharField(max_length=100)
    plan = models.CharField(max_length=100, blank=False, null=False)
    tratamiento = models.CharField(max_length=100, blank=False, null=False)
    referencias = models.CharField(max_length=2, blank=False, null=False)
    Institución = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nombre




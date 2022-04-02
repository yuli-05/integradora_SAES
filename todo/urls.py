from turtle import home
from unicodedata import name
from django import urls
from django.urls import path 
from django.urls import URLPattern, path
from .views import  Home,Historial,Nota,HojaDiaria,Medicamentos,ListadoMedicamentos, RegistrarMedicamento, EdicionMedicamento, EditarMedicamentos, EliminarMedicamentos

urlpatterns = [
    path('index/',Home, name='index'),
    path('historial/',Historial, name='historial'),
    path('nota/',Nota, name='nota'),
    path('hoja/',HojaDiaria, name='hoja'),
    path('medicamentos/',Medicamentos, name='medicamentos'),
    path('listadomedicamentos/', ListadoMedicamentos, name='listadomedicamentos'),
    path('medicamentos/registrarMedicamento/', RegistrarMedicamento, name='registrarMedicamento'),
    path('edicionMedicamentos/<int:id>', EdicionMedicamento, name='edicionMedicamentos'),
    path('editarMedicamentos/', EditarMedicamentos, name='editarMedicamentos'),
    path('eliminarMedicamentos/<int:id>', EliminarMedicamentos, name='eliminarMedicamentos'),

]
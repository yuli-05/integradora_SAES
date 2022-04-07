from turtle import home
from unicodedata import name
from django import urls
from django.urls import path 
from django.urls import URLPattern, path
from .views import  Home,Historial,Nota,HojaDiaria,Medicamentos,ListadoMedicamentos, RegistrarMedicamento, EdicionMedicamento, EditarMedicamentos, EliminarMedicamentos,  ViewMedicamento ,ListadoNota, registrarCurso, EliminarNota, EdicionNota, editarNota, ViewNota

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
    path('viewMedicamentos/<int:id>', ViewMedicamento, name='viewMedicamentos'),
    path('listadohoja/', ListadoNota, name='listadohoja'),
    path('registrarNota/', registrarCurso),
    path('eliminarNota/<int:id>', EliminarNota, name='eliminarNota'),
    path('edicionNota/<int:id>', EdicionNota, name='edicionNota'),
    path('editarNota/', editarNota, name='editarNota'),
     path('viewNota/<int:id>', ViewNota, name='viewNota'),


]
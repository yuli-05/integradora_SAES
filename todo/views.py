from django.shortcuts import redirect, render, get_object_or_404
from todo.models import ListMedicamentos,NotaDeEvolucion

# Create your views here.

def Home(request):
    return render(request,'index.html')

def Historial(request):
    return render(request,'form_historial_clinico.html')

def Nota(request):
    return render(request,'form_nota_de_evolucion.html')

def HojaDiaria(request):
    return render(request,'form_hoja_diaria.html')

def Medicamentos(request):
    return render(request,'form_medicamentos.html')

def ListadoMedicamentos(request):
    medi = ListMedicamentos.objects.all()
    return render(request, 'listado_medicamentos.html', {"medicamentos2": medi})
    #return render(request, 'listado_medicamentos.html')

def RegistrarMedicamento(request):
    id=request.POST['id']
    nombre=request.POST['nombremedicamento']
    cantidad=request.POST['cantidad']
    fecha=request.POST['fecha']

    medicamento=ListMedicamentos.objects.create(
       id=id, nombre=nombre, cantidad=cantidad, fecha=fecha)
    return redirect('/listadomedicamentos')


def EdicionMedicamento(request, id):
    medicamentos3=ListMedicamentos.objects.get(id=id)
    return render(request, "editar_medicamentos.html", {"medicamentos3": medicamentos3})

def EditarMedicamentos(request):
    id=request.POST['id']
    nombre=request.POST['nombremedicamento']
    cantidad=request.POST['cantidad']
    fecha=request.POST['fecha']

    medicamentos4=ListMedicamentos.objects.get(id=id)
    medicamentos4.nombre = nombre
    medicamentos4.cantidad = cantidad
    medicamentos4.fecha = fecha
    medicamentos4.save()

    return redirect('/listadomedicamentos')



def EliminarMedicamentos(request, id):
    medicamentoss=ListMedicamentos.objects.get(id=id)
    medicamentoss.delete()
    return redirect('/listadomedicamentos')

def ViewMedicamento(request, id):
    medicamentos3=ListMedicamentos.objects.get(id=id)
    return render(request, "view_medicamentos.html", {"medicamentos3": medicamentos3})

def ListadoNota(request):
    nota = NotaDeEvolucion.objects.all()
    return render(request, 'listado_nota.html', {"nota1": nota})

def registrarCurso(request):
    id=request.POST['id']
    fecha=request.POST['fecha']
    carrera=request.POST['carrera']
    grupo=request.POST['grupo']
    matricula=request.POST['matricula']
    nombre=request.POST['nombre']
    edad=request.POST['edad']
    sexo=request.POST['sexo']
    direccion=request.POST['direccion']
    peso=request.POST['peso']
    talla=request.POST['talla']
    presion=request.POST['presion']
    temperatura=request.POST['temperatura']
    padecimiento_actual=request.POST['padecimiento_actual']
    alegias=request.POST['alegias']
    cuales_alegias=request.POST['cuales_alegias']
    exploracion_fisica=request.POST['exploracion_fisica']
    otro=request.POST['otro']
    plan=request.POST['plan']
    tratamiento=request.POST['tratamiento']
    referencias=request.POST['referencias']
    Institución=request.POST['Institución']
    
    nota=NotaDeEvolucion.objects.create(
      id=id,  fecha=fecha, carrera=carrera, grupo=grupo, matricula=matricula, nombre=nombre, edad=edad, sexo=sexo, direccion=direccion, peso=peso, talla=talla, presion=presion, temperatura=temperatura, padecimiento_actual=padecimiento_actual, alegias=alegias, cuales_alegias=cuales_alegias, exploracion_fisica=exploracion_fisica, otro=otro, plan=plan, tratamiento=tratamiento, referencias=referencias, Institución=Institución)
    return redirect('/listadohoja')

def EdicionNota(request, id):
    nota3=NotaDeEvolucion.objects.get(id=id)
    return render(request, "editar_nota.html", {"nota3": nota3})

def editarNota(request):
    id=request.POST['id']
    fecha=request.POST['fecha']
    carrera=request.POST['carrera']
    grupo=request.POST['grupo']
    matricula=request.POST['matricula']
    nombre=request.POST['nombre']
    edad=request.POST['edad']
    sexo=request.POST['sexo']
    direccion=request.POST['direccion']
    peso=request.POST['peso']
    talla=request.POST['talla']
    presion=request.POST['presion']
    temperatura=request.POST['temperatura']
    padecimiento_actual=request.POST['padecimiento_actual']
    alegias=request.POST['alegias']
    cuales_alegias=request.POST['cuales_alegias']
    exploracion_fisica=request.POST['exploracion_fisica']
    otro=request.POST['otro']
    plan=request.POST['plan']
    tratamiento=request.POST['tratamiento']
    referencias=request.POST['referencias']
    Institución=request.POST['Institución']

    nota3=NotaDeEvolucion.objects.get(id=id)
    nota3.fecha = fecha
    nota3.carrera = carrera
    nota3.grupo = grupo
    nota3.matricula = matricula
    nota3.nombre = nombre
    nota3.edad = edad
    nota3.sexo = sexo
    nota3.direccion= direccion
    nota3.peso = peso
    nota3.talla = talla
    nota3.presion = presion
    nota3.temperatura = temperatura
    nota3.padecimiento_actual = padecimiento_actual
    nota3.alegias = alegias
    nota3.cuales_alegias = cuales_alegias
    nota3.exploracion_fisica = exploracion_fisica
    nota3.otro = otro
    nota3.plan = plan
    nota3.tratamiento = tratamiento
    nota3.referencias = referencias
    nota3.Institución = Institución

    nota3.save()
    return redirect('/listadohoja')

def ViewNota(request, id):
    nota3=NotaDeEvolucion.objects.get(id=id)
    return render(request, "view_nota.html", {"nota3": nota3})

def EliminarNota(request, id):
    nota2=NotaDeEvolucion.objects.get(id=id)
    nota2.delete()
    return redirect('/listadohoja')
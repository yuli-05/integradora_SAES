from django.shortcuts import redirect, render
from todo.models import ListMedicamentos

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

    medicamentos3=ListMedicamentos.objects.get(id=id)
    medicamentos3.nombre = nombre
    medicamentos3.cantidad = cantidad
    medicamentos3.fecha = fecha
    medicamentos3.save()

    return redirect('/listadomedicamentos')


def EliminarMedicamentos(request, id):
    medicamentoss=ListMedicamentos.objects.get(id=id)
    medicamentoss.delete()
    return redirect('/listadomedicamentos')
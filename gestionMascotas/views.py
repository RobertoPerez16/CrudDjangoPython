from django.shortcuts import render, redirect
from .models import Mascota

# Create your views here.

def home(request):
    mascotas = Mascota.objects.all()
    return render(request, 'listar.html', { "mascotas": mascotas })

def crear(request):
    return render(request, 'crear.html')

def guardar(request):

    if request.method == 'POST':
        codigo = request.POST['codmascota']
        nombre = request.POST['nombre']
        raza = request.POST['raza']
        edad = request.POST['edad']

        mascota = Mascota.objects.create(
            codigo=codigo,
            nombre=nombre,
            raza=raza,
            edad=edad
        )


    return redirect('/')

def editar(request, codigo):
    mascota = Mascota.objects.get(codigo=codigo)
    return render(request, "editar.html", {"mascota": mascota})

def actualizar(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    raza = request.POST['raza']
    edad = request.POST['edad']
    mascota = Mascota.objects.get(codigo=codigo)
    mascota.nombre = nombre
    mascota.raza = raza
    mascota.edad = edad
    mascota.save()
    return redirect('/')

def eliminar(request, codigo):
    mascota = Mascota.objects.get(codigo=codigo)
    mascota.delete()
    return redirect('/')


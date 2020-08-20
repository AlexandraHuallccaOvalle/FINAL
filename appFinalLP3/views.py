from django.shortcuts import render, HttpResponse, redirect
from appFinalLP3.models import Curso, Carrera, Estudiante

# Create your views here.
def index(request):
   return render(request, 'index.html')

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request,'cursos.html',{
        'cursos': cursos,
        'titulo' : 'Listado de Cursos'
    })
def carreras(request):
   return render(request, 'carreras.html')

def estudiantes(request):
   return render(request, 'estudiantes.html')

def consultas(request):
   return render(request, 'consultas.html')
def save_cursos(request,codigo,nombre,horas,creditos,estado):
    cursos = Curso(
        codigo = codigo,
        nombre = nombre,
        horas = horas,
        creditos = creditos,
        estado = estado,
    )
    cursos.save()
    return HttpResponse(F"Curso Creado: {cursos.codigo}-{cursos.nombre}")

def eliminar_cursos(request,id):
    cursos = Curso.objects.get(pk=id)
    cursos.delete()
    return redirect('cursos')

def save_carrera(request,nombre,nombrecorto,fecha_fundacion,estado):
    carreras = Carrera(
        nombre = nombre,
        nombrecorto = nombrecorto,
        fecha_fundacion = fecha_fundacion,
        estado = estado,
    )
    carreras.save()
    return HttpResponse(F"Carrera Creado: {carreras.nombre}-{carreras.nombrecorto}")

def listar_carreras(request):
    carreras = Carrera.objects.all()
    return render(request,'carreras.html',{
        'carreras': carreras,

    })
def eliminar_carreras(request,id):
    carreras = Carrera.objects.get(pk=id)
    carreras.delete()
    return redirect('carreras')

def save_estudiante(request,codigo,nombre,apellidos,dni,direccion,fecha_nacimiento,estado):
    estudiantes = Estudiante(
        codigo = codigo,
        nombre = nombre,
        apellidos = apellidos,
        dni = dni,
        direccion = direccion,
        fecha_nacimiento = fecha_nacimiento,
        estado = estado,
    )
    estudiantes.save()
    return HttpResponse(F"Carrera Creado: {estudiantes.nombre}-{estudiantes.apellidos}")

def listar_estudiante(request):
    estudiantes = Estudiante.objects.all()
    return render(request,'estudiantes.html',{
        'estudiantes': estudiantes,

    })
def eliminar_estudiante(request,id):
    estudiantes = Estudiante.objects.get(pk=id)
    estudiantes.delete()
    return redirect('estudiantes')
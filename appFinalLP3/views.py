from django.shortcuts import render, HttpResponse, redirect
from appFinalLP3.models import Curso

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

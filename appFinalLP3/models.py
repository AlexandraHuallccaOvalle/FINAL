from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo=models.IntegerField(unique=True)
    nombre=models.CharField(max_length=100)
    horas=models.IntegerField()
    creditos=models.CharField(max_length=100)
    estado=models.CharField(max_length=1)

class Carrera(models.Model):
    nombre=models.CharField(max_length=100)
    nombrecorto=models.CharField(max_length=30)
    fecha_fundacion=models.CharField(max_length=10)
    estado=models.CharField(max_length=1)

class Estudiante(models.Model):
    codigo=models.CharField(max_length=100)
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    dni=models.CharField(max_length=10)
    direccion=models.CharField(max_length=100)
    fecha_nacimiento=models.CharField(max_length=10)
    estado=models.CharField(max_length=1)
    
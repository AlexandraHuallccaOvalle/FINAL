"""proyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appFinalLP3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('cursos/',views.listar_cursos,name="cursos"),
    path('carreras/', views.listar_carreras, name="carreras"),
    path('estudiantes/', views.listar_estudiante, name="estudiantes"),
    path('consultas/', views.consultas, name="consultas"),
    path('eliminar_cursos/<int:id>',views.eliminar_cursos,name="eliminar_cursos"),
    path('crear_carreras/<str:nombre>/<str:nombrecorto>/<str:fecha_fundacion>/<str:estado>',views.save_carrera,name="crear_carreras"),
    path('crear_estudiante/<str:codigo>/<str:nombre>/<str:apellidos>/<str:dni>/<str:direccion>/<str:fecha_nacimiento>/<str:estado>',views.save_estudiante,name="crear_estudiantes"),

]

from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("inicio/", inicio, name = "coder-inicio"),
    path("estudiantes/", estudiantes, name = "coder-estudiantes"),
    path("profesores/", profesores, name = "coder-profesores"),
    path("cursos/", cursos, name = "coder-cursos"),
    path("profesores/crear/", creacion_profesores, name = "coder-profesores-crear"),
    path("cursos/crear/", creacion_curso, name = "coder-cursos-crear"),
    path("cursos/buscar", buscar_curso, name = "coder-cursos-buscar"),
    path("cursos/buscar/resultados", resultados_busqueda_cursos, name = "coder-cursos-buscar-resultados"),
    path("entregables/", entregables, name = "coder-entregables"),
]
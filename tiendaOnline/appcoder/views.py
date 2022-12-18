from django.http import HttpResponse
from django.shortcuts import render
from appcoder.models import curso, Profesor
from appcoder.forms import ProfesorFormulario

def inicio(request):
    return render(request, "appcoder/index.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def entregables(request):
    return render(request, "appcoder/entregables.html")

def creacion_curso(request):

    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = int(request.POST["camada"])
        Curso = curso(nombre = nombre_curso, camada = numero_camada)
        Curso.save()

    return render(request, "appcoder/curso_formulario.html")

def creacion_profesores(request):

    if request.method == "POST":

        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            profesor = Profesor(nombre = data["nombre"], apellido = data["apellido"], email = data["email"], profesion = data["profesion"])

            profesor.save()

    formulario = ProfesorFormulario()

    contexto = {"formulario": formulario}
    return render(request, "appcoder/profesores_formularios.html", contexto)

def resultados_busqueda_cursos(request):

    nombre_curso = request.GET["nombre_curso"]

    cursos = curso.objects.filter(nombre__icontains = nombre_curso)

    return render(request, "appcoder/resultados_busqueda_cursos.html", {"cursos": cursos})

def buscar_curso(request):

    return render(request, "appcoder/busqueda_cursos.html")

# Create your views here.

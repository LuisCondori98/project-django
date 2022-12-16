from django.http import HttpResponse
from django.shortcuts import render

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

# Create your views here.

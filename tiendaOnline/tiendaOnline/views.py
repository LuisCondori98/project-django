from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola desarrollador...!")

def diahoy (request, nombre):
    hoy = datetime.now()

    respuesta = f"hoy es {hoy} - Bienvenido {nombre}"
    return HttpResponse(respuesta)

def anio_nacimiento(request, edad):
    edad = int(edad)

    anio_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en {anio_nac}")

def plantilla(request):
    archivo = open("/Users/lcond/OneDrive/Documentos/-- CODERHOUSE --/PYTHON/proyecto-django/tiendaOnline/tiendaOnline/templates/plantilla.html")

    plantilla = Template(archivo.read())

    archivo.close()

    datos = {"nombre": "Luis", "fecha": datetime.now(), "apellido": "Condori"}

    contexto = Context(datos)

    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)

def vista_listado_alumnos(request):
    archivo = open(r"C:\Users\lcond\OneDrive\Documentos\-- CODERHOUSE --\PYTHON\proyecto-django\tiendaOnline\tiendaOnline\templates\listado_alumno.html")

    plantilla = Template(archivo.read())

    archivo.close()

    listado_alumnos = ["Luis Condori", "Isaac Anaya", "Jose Quispe", "Daniel Rojas", "Valiat Linare", "Piero Matos", "Alonso Cardenas", "Jhosep Serpa", "Fernando Yupanqui", "Alvaro Gutierrez", "Axel Casas"]

    datos = {"materia": "PHP", "listado_alumnos": listado_alumnos}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def vista_listado_alumnos2(request):
    listado_alumnos = ["Luis Condori", "Isaac Anaya", "Jose Quispe", "Daniel Rojas", "Valiat Linare", "Piero Matos"]

    datos = {"materia": "PHP", "listado_alumnos": listado_alumnos}

    plantilla = loader.get_template("listado_alumno.html")
    documento = plantilla.render(datos)

    return HttpResponse(documento)


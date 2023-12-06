from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): #primera vista
    p1 = Persona("Profesor Juan", "Díaz")

    ahora = datetime.datetime.now()

    temasDelCurso = ["Plantillas", "Modelos", "Formularios", "Vista", "Despliegue"]

    doc_externo = open("C:/Users/bmenendez_red.COORDINACION/Desktop/DjangoProjects/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasDelCurso})

    documento = plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Nos vemos en el proximo capitulo del curso")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, agno):
    #edadActual = 18
    periodo = agno - 2019
    edadFutura = edad + periodo

    documento = """<html>
    <body>
    <h2>
    En el año %s tendrás %s años""" %(agno, edadFutura)

    return HttpResponse(documento)
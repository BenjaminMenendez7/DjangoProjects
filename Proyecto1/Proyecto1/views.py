from django.http import HttpResponse
import datetime

def saludo(request): #primera vista
    documento = """<html>
    <body>
    <h1>
    Hola Alumnos esta es nuestra primera pagina con Django
    </h1>
    </body>
    </html>"""

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

from django.http import HttpResponse
import datetime
def saludo(request): #primera Vista
    
    documento="""<html>
    <body>
    <h1>
    hola que talca
    </h1>
    </body>
    </html>

    """

    return HttpResponse(documento)

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    hola que talca %s
    </h1>
    </body>
    </html>

    """% fecha_actual

    return HttpResponse(documento)
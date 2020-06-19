from django.http import HttpResponse
import datetime
from django.shortcuts import *



def saludo(request): #primera Vista

    return render(request,"plantilla.html")

from django.shortcuts import render, HttpResponse
from servicio.models import Servicio

# Create your views here.

def home(request):
    return render(request, "cafeWebApp/home.html")

def servicios(request):
    servicios=Servicio.objects.all()
    return render(request, "cafeWebApp/servicios.html", {"servicios": servicios})

def tienda(request):
    return render(request, "cafeWebApp/tienda.html")

def contacto(request):
    return render(request, "cafeWebApp/contacto.html")
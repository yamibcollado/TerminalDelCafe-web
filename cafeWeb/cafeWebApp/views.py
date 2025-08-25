from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "cafeWebApp/home.html")

def servicios(request):
    return render(request, "cafeWebApp/servicios.html")

def tienda(request):
    return render(request, "cafeWebApp/tienda.html")

def contacto(request):
    return render(request, "cafeWebApp/contacto.html")
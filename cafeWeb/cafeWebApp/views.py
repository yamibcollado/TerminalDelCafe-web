from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "cafeWebApp/home.html")

def tienda(request):
    return render(request, "cafeWebApp/tienda.html")


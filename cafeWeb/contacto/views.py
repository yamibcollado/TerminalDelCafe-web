from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    formulario = FormularioContacto()
    
    if request.method == "POST":
        formulario = FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get("nombre")
            email = formulario.cleaned_data.get("email")
            contenido = formulario.cleaned_data.get("contenido")
            
            # Aquí podrías guardar la info o enviarla por email
            messages.success(request, "¡La información fue enviada correctamente!")
            
            return redirect("contacto")  
    
    return render(request, "contacto/contacto.html", {'form': formulario})


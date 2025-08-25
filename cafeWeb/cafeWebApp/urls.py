from django.urls import path
from cafeWebApp import views

#Urls de todas las aplicaciones que tenga el proyecto.
#enlaces de nuestra aplicacion "cafeWebApp"
urlpatterns = [
    path('', views.home, name="home"),
    path('servicios', views.servicios, name="servicios"),
    path('tienda', views.tienda, name="tienda"),
    path('contacto', views.contacto, name="contacto"),
]
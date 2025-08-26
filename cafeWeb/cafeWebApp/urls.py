from django.urls import path
from cafeWebApp import views
from django.conf import settings
from django.conf.urls.static import static

#Urls de todas las aplicaciones que tenga el proyecto.
#enlaces de nuestra aplicacion "cafeWebApp"
urlpatterns = [

    path('', views.home, name="home"),
    path('servicios', views.servicios, name="servicios"),
    path('tienda', views.tienda, name="tienda"),
    path('contacto', views.contacto, name="contacto"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
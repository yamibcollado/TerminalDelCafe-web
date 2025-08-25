
from django.contrib import admin
from django.urls import include, path



#Urls de TODAS las aplicaciones que tenga el proyecto.
urlpatterns = [
    path('admin/', admin.site.urls),

    #enlace a urls de nuestra aplicacion "cafeWebApp"
    path('', include('cafeWebApp.urls')),
    
]

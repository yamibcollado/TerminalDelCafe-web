from django.contrib import admin
from .models  import Servicio


#importamos la aplicacion de servicio en el panel administrador.
#registramos el modelo.

admin.site.register(Servicio)


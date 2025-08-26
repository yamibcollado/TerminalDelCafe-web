from django.db import models


class Servicio(models.Model):
    titulo=models.CharField(max_length=20)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField()
    precio=models.IntegerField()

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):
        return self.titulo

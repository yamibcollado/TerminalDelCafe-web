from django.db import models

class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name='categoriaProd'
        verbose_name_plural='categoriasProd'

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre=models.CharField(max_length=20)
    categoria=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'


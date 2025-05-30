from django.db import models

# Create your models here.


class Pedido(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.PositiveSmallIntegerField()
    imagen_url = models.URLField(blank=True)

    def __str__(self):
        return self.nombre
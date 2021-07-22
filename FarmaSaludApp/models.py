from django.db import models
from django.db.models.fields.files import FileField

class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True,verbose_name='Codigo')
    nombre_cat = models.CharField(max_length=100,verbose_name='Categoria')
    def __str__(self):
        return self.nombre_cat
class Producto(models.Model):
    id_pro = models.AutoField(primary_key=True,verbose_name='Codigo')
    nombre_pro = models.CharField(max_length=100,verbose_name='Nombre')
    cantidad_pro = models.PositiveIntegerField(verbose_name='Cantidad')
    precio_pro = models.FloatField(verbose_name='Precio')
    imagen_pro=models.CharField(max_length=100, verbose_name='Imagen', null=True)
    fk_id_cat= models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
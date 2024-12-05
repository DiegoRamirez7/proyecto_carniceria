from django.db import models

# Create your models here.

class Productos(models.Model):
    id_producto = models.PositiveIntegerField(primary_key=True)
    nombre_producto= models.CharField(max_length=30)
    fecha_ingreso=models.DateTimeField()
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)  
    descripcion_producto=models.CharField(max_length=20)
    stock= models.PositiveIntegerField()
    id_proveedor=models.PositiveIntegerField()


    def __str__(self):
        return self.id_producto
from django.db import models

# Create your models here.

class Clientes(models.Model):
    id_cliente = models.PositiveIntegerField(primary_key=True)
    nombre_cliente = models.CharField(max_length=20)
    direccion_cliente=models.CharField(max_length=50)
    correo_electronico=models.EmailField(max_length=50)
    fecha_registro=models.DateField()
    tipo_cliente=models.CharField(max_length=20)
    telefono_cliente=models.PositiveBigIntegerField()


    def __str__(self):
        return self.id_cliente
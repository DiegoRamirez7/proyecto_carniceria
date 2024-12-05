from django.db import models

# Create your models here.

class Proveedores(models.Model):
    id_proveedor = models.PositiveIntegerField(primary_key=True)  # ID único del proveedor
    telefono_proveedor = models.PositiveBigIntegerField()  # Teléfono del proveedor
    direccion_proveedor = models.CharField(max_length=100)  # Dirección con más espacio
    contacto_principal = models.CharField(max_length=50)  # Contacto principal del proveedor
    correo_electronico = models.EmailField(max_length=100)  # Campo con validación de email
    nombre_proveedor = models.CharField(max_length=100)  # Nombre del proveedor
    
    def __str__(self):
        return self.id_proveedor
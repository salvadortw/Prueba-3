from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class AgenteVentas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.user.username

class ClientePotencial(models.Model):
    RUT = models.CharField(max_length=12, unique=True)
    nombre_completo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo

class ClienteVigente(models.Model):
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_completo

class CasoCliente(models.Model):
    rut_cliente = models.CharField(max_length=12)
    nombre = models.CharField(max_length=255, default='')
    descripcion_caso = models.TextField()
    fecha = models.DateField(default=date.today) 
    
    # Definir opciones para el campo 'estado'
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Resuelto', 'Resuelto'),
    ]
    
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    
    def __str__(self):
        return f"Caso {self.id} - {self.rut_cliente}"
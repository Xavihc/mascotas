from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.db.models.base import Model
from django.forms import BooleanField, CharField, DateField, IntegerField


# Create your models here.
class Tipo_usuario(models.Model):
    tipo = models.CharField(max_length=64)
    descuento = models.IntegerField(default=0)

    def __str__(self):
        return self.tipo 

class Usuario(models.Model):
    rut = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=128)
    tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.nombre

class Tipo_producto(models.Model):
    nombre = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    tipo_producto = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100,default='')
    precio = models.IntegerField(default=0)
    precio_costo = models.IntegerField(default=0)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    descripcion= models.CharField(max_length=600,default='')
    imagen = models.ImageField(upload_to="porductos", null= True)

    def __str__(self):
        return f'{self.nombre}  -->  {self.precio}'


class Despacho(models.Model):
    estado = models.CharField(max_length=64)

    def __str__(self):
        return self.estado

class MedioPago(models.Model):
    nombre = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha = models.DateField(auto_now=True)
    total = models.IntegerField()
    direccion_despacho = models.CharField(max_length=500)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    estado_despacho = models.ForeignKey(Despacho, on_delete=models.CASCADE, default=1)
    notas = models.TextField(max_length=600)
    medio_pago = models.ForeignKey(MedioPago, on_delete=models.CASCADE)

    def __str__(self):
        return self.total

class detalleVenta(models.Model):
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

    def __str__(self):
        return self.subtotal

class Donacion(models.Model):
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fecha} --> ${self.cantidad}"

class detalleDonacion(models.Model):
    id_donacion = models.ForeignKey(Donacion, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id_usuario} dono ${self.cantidad}'

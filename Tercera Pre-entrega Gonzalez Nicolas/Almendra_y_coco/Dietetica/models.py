from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField(max_length=40)
    DNI= models.IntegerField()
    

    def __str__(self):
        return f"Cliente {self.nombre} {self.apellido}"

class Vendedores(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField(max_length=40)
    DNI= models.IntegerField()
    direccion= models.CharField(max_length=40)

    def __str__(self):
        return f"Vendedor {self.nombre} {self.apellido}"


class Productos(models.Model):
    nombre= models.CharField(max_length=40)
    cantidad= models.IntegerField()
    precio= models.IntegerField()

    def __str__(self):
        return f"{self.nombre} por {self.cantidad}"

class ProductosPorMayor(models.Model):
    nombre= models.CharField(max_length=40)
    cantidad= models.IntegerField()
    precio= models.IntegerField()

    def __str__(self):
        return f"{self.nombre} por {self.cantidad}"

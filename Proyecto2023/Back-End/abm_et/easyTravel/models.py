from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nperfil = models.IntegerField(blank=False)
    nombre = models.CharField(max_length=100, blank=False)
    apellidos = models.CharField(max_length=100, blank=False)
    fecha_nac= models.DateField(blank=False)
    celular= models.CharField(max_length=100, blank=False)
    mail=models.CharField(max_length=100, blank=False)
    puntaje= models.IntegerField(blank=False, default=0)
    class Meta:
        db_table = "Usuario"
        verbose_name="Usuarios de EasyTravel"
        verbose_name_plural="Usuarios"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre 

class Categoria(models.Model):

    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.TextField(max_length=1000, blank=False)
    class Meta:
        db_table="Categoria"
        verbose_name="Categoria de productos"
        verbose_name_plural="Categorias"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    codigodeBarras = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.TextField(max_length=1000, blank=False)
    precio = models.DecimalField(max_length=10, blank=False, decimal_places=2, max_digits=10)
    cantidad = models.IntegerField(blank=False, default=0)
    fecha_inicio= models.DateField(blank=False)
    fecha_fin= models.DateField(blank=False)
    id_categoria = models.ForeignKey(Categoria,to_field="id_categoria",on_delete=models.CASCADE)
    class Meta:
        db_table = "Producto"
        verbose_name="Productos de EasyTravel"
        verbose_name_plural="Productos"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre   
    
    class CarritoCompras(models.Model):
        producto_nombre = models.CharField(max_length=200)
        producto_precio = models.DecimalField(max_length=10, blank=False, decimal_places=2, max_digits=10)
        producto_cantidad = models.PositiveIntegerField()
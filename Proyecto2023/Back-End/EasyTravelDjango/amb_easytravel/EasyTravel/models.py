from django.db import models

# Create your models here.
class Usuarios(models.Model):
    ID_USUARIO= models.AutoField(primary_key=True)
    NOMBRE= models.CharField(max_length=30, blank=False)
    APELLIDOS= models.CharField(max_length=30, blank=False)
    FECH_NAC= models.DateField(blank=False)
    DNI= models.IntegerField(max_length=30)
    PASS= models.CharField(max_length=30, blank=False)
    NPERFIL= models.CharField
    MAIL = models.CharField(max_length=30, blank=False)
    CELULAR= models.CharField(max_length=30, blank=False)
    PUNTAJE= models.IntegerField
   
    
    class Meta:
        db_table="Usuario"
        verbose_name= "Usuario de EasyTravel"
        verbose_name_prural= "Usuarios creados de EasyTravel"
    def _unicode_(self):
        return self.nombre
    def _str_(self):
        return self.nombre
    
class Producto(models.Model):
    ID_PRODUCTO= models.AutoField(primary_key=True)
    NOMBRE= models.CharField(max_length=50, blank=False)
    DETALLE= models.CharField(max_length=100, blank=False)
    FECHA_INICIO= models.DateField(blank=False)
    FECHA_FIN= models.DateField(blank=False)
    ACTIVO= models.BooleanField(blank=False)
    PRECIO= models.IntegerField(blank=False)
    CANTIDAD=models.IntegerField(blank=False, default=0)
    
    class Meta:
        db_table="Producto"
        verbose_name= "Productos de EasyTravel"
        verbose_name_prural= "Productos disponibles en EasyTravel"
    def _unicode_(self):
        return self.nombre
    def _str_(self):
        return self.nombre
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
        verbose_name= "Usuarios de EasyTravel"
        verbose_name_prural="Usuarios"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    ID_CATEGORIA= models.AutoField(primary_key=True)
    NOMBRE= models.CharField(max_length=50, blank=False)
    DETALLE= models.CharField(max_length=100, blank=False)
    CANTIDAD=models.IntegerField(blank=False, default=0)
    
    class Meta:
        db_table="Categoria"
        verbose_name= "Categorias de Productos"
        verbose_name_prural="Categorias"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre


    
class Producto(models.Model):
    ID_PRODUCTO= models.AutoField(primary_key=True)
    NOMBRE= models.CharField(max_length=50, blank=False)
    DETALLE= models.CharField(max_length=100, blank=False)
    FECHA_INICIO= models.DateField(blank=False)
    FECHA_FIN= models.DateField(blank=False)
    ACTIVO= models.BooleanField(blank=False)
    PRECIO= models.DecimalField(max_length=10, decimal_places=2,blank=False)
    CANTIDAD=models.IntegerField(blank=False, default=0)
    ID_CATEGORIA = models.ForeignKey(Categoria,to_field="ID_CATEGORIA", on_delete=models.CASCADE)

    
    class Meta:
        db_table="Producto"
        verbose_name= "Productos de EasyTravel"
        verbose_name_prural="Productos"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    


    
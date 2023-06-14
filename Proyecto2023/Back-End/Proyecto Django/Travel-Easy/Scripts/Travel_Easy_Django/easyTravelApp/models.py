from django.db import models

# Create your models here.
class TIPOS_DNI(models.Model):
    DNI_ID = models.AutoField(primary_key=True)
    DNI_ACTIVO= models.BooleanField
    DNI_DESCRIPTION= models.CharField(max_length=30)

    class Meta:
        db_table="TIPOS_DNI"
        verbose_name= "Tipos de DNI"
        verbose_name_prural= "Tipos de DNI"
    def _unicode_(self):
        return self.nombre
    def _str_(self):
        return self.nombre


class Producto(models.Model):
    PROD_ID = models.AutoField(primary_key=True)
    PROD_NOMBRE= models.CharField(max_length=50, blank=False)
    PROD_DETALLE= models.CharField(max_length=100, blank=False)
    PROD_FECHA_INICIO= models.DateField(blank=False)
    PROD_FECHA_FIN= models.DateField(blank=False)
    PROD_ACTIVO= models.BooleanField(blank=False)
    PROD_PRECIO= models.IntegerField(blank=False)
    
    class Meta:
        db_table="Productos"
        verbose_name= "Productos de EasyTravel"
        verbose_name_prural= "Productos disponibles en EasyTravel"
    def _unicode_(self):
        return self.nombre
    def _str_(self):
        return self.nombre
    

    class Usuarios(models.Model):
        USU_ID= models.AutoField(primary_key=True)
        USU_NOMBRES= models.CharField(max_length=30, blank=False)
        USU_APELLIDOS= models.CharField(max_length=30, blank=False)
        USU_FECH_NAC= models.DateField(blank=False)
        USU_DNI= models.IntegerField(max_length=30)
        USU_PASS= models.CharField(max_length=30, blank=False)
        USU_NPERFIL= models.CharField
        USU_MAIL = models.CharField(max_length=30, blank=False)
        USU_CELULAR= models.CharField(max_length=30, blank=False)
        USU_PUNTAJE= models.IntegerField
        DNI_ID= models.ForeignKey(TIPOS_DNI,to_field='DNI_ID',on_delete=models.CASCADE)
    
    class Meta:
        db_table="Usuario"
        verbose_name= "Usuario de EasyTravel"
        verbose_name_prural= "Usuarios creados de la EasyTravel"
    def _unicode_(self):
        return self.nombre
    def _str_(self):
        return self.nombre
    


    class Combos(models.Model):
        T_COMB_ID = models.IntegerField(primary_key=True, blank=False)
        T_COMB_FECH_INI = models.DateTimeField(unique_for_date=None, blank=False)
        T_COMB_FECH_FIN = models.DateTimeField(unique_for_date=None, blank=False)
        T_COMB_PRECIO = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
        T_COMB_NOMBRE= models.CharField(max_length=50, blank=False)
        T_COMB_DETALLE = models.CharField(max_length=500, blank=False)
        T_COMB_ACTIVO = models.BooleanField(default=False)
        T_COMB_PORC_RESERVA = models.DecimalField(max_digits=10, decimal_places=2)
        T_COMB_FECHA_HORA_RESERVA = models.DateTimeField(unique_for_date=None, blank=False) 


class Meta:
        db_table = "Combos"
        verbose_name = "Combo"
        verbose_name_plural = "Combos"

        def __unicode__(self):
         return self.nombre

        def __str__(self):
            return self.nombre


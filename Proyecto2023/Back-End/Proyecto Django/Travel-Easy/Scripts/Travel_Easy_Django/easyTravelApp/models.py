from django.db import models

# Create your models here.
class Usuarios(models.Model):
    USU_ID = models.AutoField(primary_key=True)
    USU_NOMBRES= models.CharField(max_length=30, blank=False)
    USU_APELLIDOS= models.CharField(max_length=30, blank=False)
    USU_FECH_NAC= models.DateField(blank=False)
    USU_DNI= models.IntegerField(max_length=30)
    USU_PASS= models.CharField(max_length=30, blank=FALSE)
    USU_NPERFIL= models.CharField
    USU_MAIL = models.CharField(max_length=30, blank=False)
    USU_CELULAR= models.CharField(max_length=30, blank=False)
    USU_PUNTAJE= models.IntegerField
    
    class Meta:
        db_table="Usuario"
        verbose_name= "Usuario de EasyTravel"
        verbose_name_prural= "Usuarios creados de la EasyTravel"
    def _unicode_(self):
        return self.nombre
    def _str_(self):
        return self.nombre


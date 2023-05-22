from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_Usuario = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=20, blank=False)
    apellido= models.CharField(max_length=20, blank=False)
    mail = models.CharField(max_length=30, blank=False)
    
    class Meta:
        db_table="Usuario"
        verbose_name= "Usuario de EasyTravel"
        verbose_name_prural= "Usuarios creados de la EasyTravel"
    def _unicode_(self):
        return self.nombre
    def _str_(self):
        return self.nombre


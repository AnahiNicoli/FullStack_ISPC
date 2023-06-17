from django.contrib import admin
from .models import Usuario
from .models import Categoria
from .models import Producto

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nperfil", "nombre", "apellidos", "mail", "puntaje")
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre" , "descripcion")
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id_categoria", "nombre", "descripcion", "fecha_inicio", "fecha_fin", "precio", "cantidad" )

admin.site.register(Usuario,UsuarioAdmin)    
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)


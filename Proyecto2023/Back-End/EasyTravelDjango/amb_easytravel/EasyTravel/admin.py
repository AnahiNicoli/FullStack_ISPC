from django.contrib import admin
from .models import Usuarios
from .models import Categoria
from .models import Producto

# Register your models here.
class UsuariosAdmin(admin.ModelAdmin):
    list_display= ("NOMBRE","APELLIDOS","PUNTAJE")
class CategoriaAdmin(admin.ModelAdmin):
    list_display= ("NOMBRE","DETALLE","CANTIDAD")
class ProductoAdmin(admin.ModelAdmin):
    list_display= ("NOMBRE","DETALLE","FECHA_INICIO","FECHA_FIN","PRECIO","CANTIDAD")

admin.site.register(Usuarios,UsuariosAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
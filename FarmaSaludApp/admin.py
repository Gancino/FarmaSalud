from django.contrib import admin
from FarmaSaludApp.models import *
# Register your models here.
class CategoriaAdmin (admin.ModelAdmin):
    list_display=("id_cat","nombre_cat")
    search_fields=("id_cat","nombre_cat")
admin.site.register(Categoria,CategoriaAdmin)

class ProductoAdmin (admin.ModelAdmin):
    list_display=("id_pro","nombre_pro","cantidad_pro","precio_pro","imagen_pro","fk_id_cat")
    search_fields=("id","nombre_pal")
admin.site.register(Producto,ProductoAdmin)



from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'precio',
        'estado',
        'descripcion',
    ]

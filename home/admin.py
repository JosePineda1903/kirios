from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(SobreNosotros)
class SobreNosotrosAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'descripcion_titulo',
        "titulo_secundario",
        "descripcion",
        "imagen",
    ]

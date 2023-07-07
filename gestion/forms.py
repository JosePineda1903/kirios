from django import forms
from .models import *
import datetime

class ProductoForm(forms.ModelForm):
    """Form definition for ProductoForm."""

    class Meta:
        """Meta definition for ProductoForm."""

        model = Producto
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    """Form definition for categoriaForm."""

    class Meta:
        """Meta definition for CategoriaForm."""

        model = Categoria
        fields = '__all__'
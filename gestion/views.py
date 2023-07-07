from django.shortcuts import render, redirect
from django import forms
from .models import *
from gestion.forms import *

# Create your views here.
def gestion(request):
    return render(request, 'gestion/index.html')

def producto_form(request):
    producto_form = ProductoForm()

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto = producto_form.save()
            return redirect('listado_productos')
            print(producto)
        else:
            context={
            'title': "CREAR PRODUCTO",
            'producto_form':producto_form,
            }
            return redirect('producto_form')
    context={
        'title': "CREAR PRODUCTO",
        'producto_form':producto_form,
    }

    return render(request, 'gestion/productos/producto_form.html', context)

def listado_productos(request):
    title = 'Listado Productos'
    # consulta a base de datos para traer todos los productos
    productos = Producto.objects.all()
    print(productos)
    context = {
        'title':title,
        'productos':productos,
    }
    return render(request, 'gestion/productos/listado_productos.html', context)

def producto_edit(request, producto_pk):
    producto_object = Producto.objects.get(pk=producto_pk)
    producto_form = ProductoForm(instance=producto_object)

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, instance=producto_object)
        if producto_form.is_valid():
            producto = producto_form.save()
            return redirect('listado_productos')
        else:
            context = {
                'title': "EDITAR PRODUCTO",
                'producto_form':producto_form
            }
            return redirect('producto_form')

    context = {
         'title': "EDITAR PRODUCTO",
         'producto_form':producto_form
    }
    return render(request, 'gestion/productos/producto_form.html', context)


def categoria(request):
    categoria = CategoriaForm()

    if request.method == 'POST':
        categoria = CategoriaForm(request.POST)
        if categoria.is_valid():
            producto = categoria.save()
            return redirect('list_categoria')
            print(producto)
        else:
            context={
            'title': "CREAR PRODUCTO",
            'categoria':categoria,
            }
            return redirect('categoria')
    context={
        'title': "CREAR PRODUCTO",
        'categoria':categoria,
    }

    return render(request, 'gestion/productos/categoria_form.html', context)

def list_categoria(request):
    title = 'Listado Categoria'
    # consulta a base de datos para traer todos los productos
    list_categoria = Categoria.objects.all()
    print(categoria)
    context = {
        'title':title,
        'categoria':list_categoria,
    }
    return render(request, 'gestion/productos/list_categoria.html', context)

def categoria_edit(request, categoria_pk):
    categoria_object = Categoria.objects.get(pk=categoria_pk)
    categoria_form = CategoriaForm(instance=categoria_object)

    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST, instance=categoria_object)
        if categoria_form.is_valid():
            categoria = categoria_form.save()
            return redirect('list_categoria')
        else:
            context = {
                'title': "EDITAR categoria",
                'categoria':categoria_form
            }
            return redirect('categoria_form')

    context = {
         'title': "EDITAR categoria",
         'categoria':categoria_form
    }
    return render(request, 'gestion/productos/categoria_form.html', context)




def producto_delete(request, producto_pk):
    producto_object = Producto.objects.get(pk=producto_pk)
    if request.method == 'POST':
        producto_object.delete()
        return redirect('listado_productos')
    context = {
        'title': "Eliminar Producto",
        'producto_object':producto_object
    }
    return render(request, 'gestion/productos/producto_delete.html', context)

def categoria_delete(request, categoria_pk):
    categoria_object = Categoria.objects.get(pk=categoria_pk)
    if request.method == 'POST':
        categoria_object.delete()
        return redirect('list_categoria')
    context = {
        'title': "Eliminar categoria",
        'categoria_object':categoria_object
    }
    return render(request, 'gestion/productos/categoria_delete.html', context)
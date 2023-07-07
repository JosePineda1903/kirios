from django.urls import path
from . import views
urlpatterns=[
    path('gestion/', views.gestion, name='gestion'),
    path('producto_form/', views.producto_form, name='producto_form'),
    path('listado_productos/', views.listado_productos, name='listado_productos'),
    path('producto_edit/<int:producto_pk>', views.producto_edit, name='producto_edit'),
    path('producto_delete/<int:producto_pk>', views.producto_delete, name='producto_delete'),
    path('categoria/', views.categoria, name='categoria'),
    path('list_categoria/', views.list_categoria, name='list_categoria'),
    path('categoria_edit/<int:categoria_pk>', views.categoria_edit, name='categoria_edit'),
    path('categoria_delete/<int:categoria_pk>', views.categoria_delete, name='categoria_delete'),
] 

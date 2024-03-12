from django.urls import path, include
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('Vendedores/', vendedores, name="Vendedores"),
    path('Clientes/', clientes, name="Clientes"),
    path('Productos/', productos, name="Productos"),
    path('Productos_por_mayor/', productos_por_mayor, name="Productos_por_mayor"),
    path('clientes_form/', clientesForm, name="clientes_form"),
    path('vendedores_form/', vendedoresForm, name="vendedores_form"),
    path('productos_form/', productosForm, name="productos_form"),
    path('productos_por_mayor_form/', productos_por_mayorForm, name="productos_por_mayor_form"),
    path('buscar_productos/', buscarProductos, name="buscar_productos"),
    path('encontrar_productos/', encontrarProductos, name="encontrar_productos"),
    ]

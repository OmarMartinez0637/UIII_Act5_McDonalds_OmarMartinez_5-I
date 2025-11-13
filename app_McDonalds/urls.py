from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_mcdonalds, name='inicio_mcdonalds'),

    # CLIENTES
    path('clientes/', views.ver_cliente, name='ver_cliente'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),

    # PEDIDOS
    path('pedidos/', views.ver_pedido, name='ver_pedido'),
    path('pedidos/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedidos/actualizar/<int:id_pedido>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/borrar/<int:id_pedido>/', views.borrar_pedido, name='borrar_pedido'),

    # EMPLEADOS
    path('empleados/', views.ver_empleado, name='ver_empleado'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/actualizar/<int:id_empleado>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:id_empleado>/', views.borrar_empleado, name='borrar_empleado'),
]

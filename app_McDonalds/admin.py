from django.contrib import admin
from .models import Cliente, Pedido, Empleado

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Empleado)

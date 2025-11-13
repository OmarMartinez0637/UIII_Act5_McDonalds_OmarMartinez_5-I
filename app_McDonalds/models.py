from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=15)
    horario = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Pedido(models.Model):
    ARTICULOS = [
        ('Hamburguesa', 'Hamburguesa'),
        ('Papas', 'Papas'),
        ('Refresco', 'Refresco'),
        ('Helado', 'Helado'),
    ]

    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos")
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="pedidos")
    fecha_pedido = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    forma_pago = models.CharField(max_length=50)
    articulos = models.CharField(max_length=200, default="Sin artículos")  # guardará los artículos seleccionados en texto

    def __str__(self):
        return f"Pedido {self.id_pedido} - {self.estado}"

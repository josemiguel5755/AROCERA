from django.db import models

class Representante(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombre_completo = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre_completo

    @property
    def nombre(self):
        """Propiedad para mantener compatibilidad con código existente"""
        return self.nombre_completo


class Factura(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
    ]
    
    numero_factura = models.CharField(max_length=20, unique=True)
    cedula = models.CharField(max_length=20)
    nombre_cliente = models.CharField(max_length=100)
    cantidad_sacos = models.PositiveIntegerField()
    representante = models.ForeignKey(Representante, on_delete=models.PROTECT)
    fecha = models.DateField()
    variedad = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_pago = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.numero_factura} - {self.nombre_cliente}"

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ['-fecha', 'numero_factura']
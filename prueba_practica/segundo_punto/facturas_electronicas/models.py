from django.db import models


class Factura(models.Model):
    identificador = models.IntegerField(primary_key=True)
    NIT = models.IntegerField()
    descripccion = models.TextField(verbose_name='Descripcción')
    valor_total = models.PositiveIntegerField()
    porcentaje_iva = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.identificador}, {self.descripccion}, {self.valor_total}'

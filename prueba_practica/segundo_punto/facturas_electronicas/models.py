from django.db import models


class Factura(models.Model):
    identificador = models.IntegerField('Identificador')
    NIT = models.IntegerField('NIT')
    descripccion = models.TextField('Descripcción')
    valor_total = models.PositiveIntegerField('Valor total')
    porcentaje_iva = models.PositiveIntegerField('Porcentaje de IVA')

    def __str__(self):
        return f'{self.identificador}, {self.descripccion}, {self.valor_total}'

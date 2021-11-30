from django.test import TestCase
from models import Factura

class ModelTest(TestCase):

    def test_factura(self):
        identificador: int = 12334
        NIT: int = 83883
        descripccion: str = 'Factura de prueba'
        valor_total: int = 22222
        porcentaje_iva: int = 333
        
        factura = Factura.objects.create_user(
            identificador = identificador,
            NIT = NIT,
            descripccion = descripccion,
            valor_total = valor_total,
            porcentaje_iva = porcentaje_iva
        )

        self.assertEqual(factura.identificador, identificador)
        self.assertEqual(factura.NIT, NIT)

        
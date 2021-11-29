from rest_framework import viewsets

from .serializers import FacturaSerializador
from .models import Factura


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializador
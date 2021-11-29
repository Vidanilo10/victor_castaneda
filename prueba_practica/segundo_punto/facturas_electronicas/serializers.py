from rest_framework import serializers
from .models import Factura

class FacturaSerializador(serializers.ModelSerializer):
    porcentaje_total = serializers.SerializerMethodField('obtener_porcentaje_total')
    
    def obtener_porcentaje_total(self, obj):
        return (obj.valor_total * obj.porcentaje_iva) / 100


    class Meta:
        model = Factura
        fields = '__all__'
    
    def validate(self, data):
        if data['identificador'] <= 0:
            raise serializers.ValidationError('Error, el indentificador tiene que ser positivo')
        
        if type(data['NIT']) != int:
            raise serializers.ValidationError('Error, el nit solo debe contener números')
        
        if data['valor_total'] <= 0:
            raise serializers.ValidationError('Error, el valor total debe ser positivo')
        
        if data['porcentaje_iva'] > 100:
            raise serializers.ValidationError('Error, el valor porcentaje de iva debe ser entre 0 y 100')
        
        return data
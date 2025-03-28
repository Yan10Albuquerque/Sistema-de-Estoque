from rest_framework import serializers
from .models import *

class EquipamentListCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Equipament
        fields = '__all__'
        
class EquipamentRetrieveUpdateDestroySerializers(serializers.ModelSerializer):
    class Meta:
        model = Equipament  
        fields = '__all__'
        
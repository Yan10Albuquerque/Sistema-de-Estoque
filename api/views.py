from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import *
from .models import *


class EquipamentListCreateView(generics.ListCreateAPIView):
    serializer_class = EquipamentListCreateSerializers
    queryset = Equipament.objects.all()




class EquipamentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EquipamentRetrieveUpdateDestroySerializers
    queryset = Equipament.objects.all()
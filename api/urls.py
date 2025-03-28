from django.urls import path
from .views import *

urlpatterns = [
    path('equipament/', EquipamentListCreateView.as_view(), name='equipament-list-create'),
    path('equipament/<int:pk>/', EquipamentRetrieveUpdateDestroyView.as_view(), name='equipament-retrieve-update-destroy'),
]

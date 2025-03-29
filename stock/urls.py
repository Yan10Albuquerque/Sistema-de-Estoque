from django.urls import path
from .views import *

urlpatterns = [
    path('stock/', dashboard, name='dashboard'),
    path('update/<int:equipament_id>/', UpdateDeleteEquipament, name='update_delete_equipament'),
    path('delete/<int:equipament_id>/', DeleteEquipament, name='delete_equipament'),
]


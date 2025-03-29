from django.contrib import admin
from django.urls import path, include
from stock.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', dashboard, name='dashboard'),
    path('update/<int:equipament_id>/', UpdateDeleteEquipament, name='update_delete_equipament'),
    path('delete/<int:equipament_id>/', DeleteEquipament, name='delete_equipament'),
    #path('stock/', include('stock.urls')),  
]



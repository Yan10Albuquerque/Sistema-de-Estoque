from django.urls import path
from .views import dashboard

urlpatterns = [
    path('d/', dashboard, name='dashboard'),
]


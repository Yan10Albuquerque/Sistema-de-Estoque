from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from api.models import *

# Create your views here.

def dashboard(request):
    if request.method == 'POST':
        equipament = Equipament()
        equipament.name = request.POST.get('name')
        equipament.description = request.POST.get('description')
        equipament.price = request.POST.get('price')
        equipament.stock = request.POST.get('stock')
        equipament.save()
        print(equipament)
    equipaments = Equipament.objects.all()
    return render(request, 'dashboard.html', {'equipaments': equipaments})

def UpdateDeleteEquipament(request, equipament_id):
    equipament = get_object_or_404(Equipament, id=equipament_id)
    if request.method == "POST":
        equipament.name = request.POST.get("name", equipament.name)
        equipament.description = request.POST.get("description", equipament.description)
        # Convertendo valores numéricos para evitar erros
        equipament.stock = int(request.POST.get("stock", equipament.stock))
        equipament.price = float(request.POST.get("price", equipament.price))
        equipament.save()
        return redirect('dashboard')  # Redireciona para a página principal
    

def DeleteEquipament(request, equipament_id):
    equipament = get_object_or_404(Equipament, id=equipament_id)
    equipament.delete()
    return redirect('dashboard')  # Redireciona para a página principal



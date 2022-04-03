from django.shortcuts import render, redirect
from .models import Clientes

# Create your views here.
def home(request):
    clientes=Clientes.objects.all()
    return render(request,"index.html",{"Clientes":clientes})

def RegistrarVehiculo(request):
    piso=request.POST['pisos']
    telefono=request.POST['telefono']
    
    client=Clientes.objects.create(piso=piso,telefono=telefono)
    return redirect('/')
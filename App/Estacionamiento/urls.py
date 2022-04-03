from django.urls import path
from . import views

urlpatterns=[
    path('', views.home),
    path('RegistrarVehiculo/',views.RegistrarVehiculo)
]
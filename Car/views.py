from django.shortcuts import render

from Car.serializers import CarSerializer
from .models import Car
from rest_framework import routers, serializers, viewsets
from django.contrib import admin



class CarsViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer  

from django.shortcuts import render
from rest_framework import generics
from .models import Cars, Category
from .serializers import CarsSerializer

class CarsAPIView(generics.ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

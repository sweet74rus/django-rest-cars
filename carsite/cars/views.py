from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cars, Category
from .serializers import CarsSerializer

class CarsAPIView(APIView):
    def get(self, request):
        l = Cars.objects.all().values()
        return Response({'cars': list(l)})

# class CarsAPIView(generics.ListAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer

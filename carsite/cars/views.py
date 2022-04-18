from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cars, Category
from .serializers import CarsSerializer

class CarsAPIView(APIView):
    def get(self, request):
        l = Cars.objects.all()
        return Response({'cars': CarsSerializer(l, many=True).data})

    def post(self, request):
        serializer = CarsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        car_new = Cars.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            body_type=request.data['body_type'],
            engine_type=request.data['engine_type'],
            color=request.data['color'],
            price=request.data['price'],
            cat_id=request.data['cat_id']
        )

        return Response({'car': CarsSerializer(car_new).data})


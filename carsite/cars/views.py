from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cars, Category
from .serializers import CarsSerializer


class CarsViewSet(viewsets.ModelViewSet):
    serializer_class = CarsSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Cars.objects.all()[:3]

        return Cars.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def show_categories(self, request, pk=None):
        categories = Category.objects.get(pk=pk)

        return Response({"categories": categories.name})

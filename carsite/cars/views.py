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
        serializer.save()

        return Response({'car': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Cars.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = CarsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Cars.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        instance.delete()

        return Response({"car": "delete car" + str(pk)})

from rest_framework import serializers
from .models import *


class CarsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body_type = serializers.CharField(max_length=255)
    engine_type = serializers.CharField(max_length=255)
    color = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    description = serializers.CharField()
    cat_id = serializers.IntegerField()


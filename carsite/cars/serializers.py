from rest_framework import serializers
from .models import *


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('__all__')

    # title = serializers.CharField(max_length=255)
    # body_type = serializers.CharField(max_length=255)
    # engine_type = serializers.CharField(max_length=255)
    # color = serializers.CharField(max_length=255)
    # price = serializers.IntegerField()
    # description = serializers.CharField()
    # cat_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Cars.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.body_type = validated_data.get("body_type", instance.body_type)
    #     instance.engine_type = validated_data.get("engine_type", instance.engine_type)
    #     instance.color = validated_data.get("color", instance.color)
    #     instance.price = validated_data.get("price", instance.price)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.cat_id = validated_data.get("cat_id", instance.cat_id)
    #     instance.save()
    #     return instance

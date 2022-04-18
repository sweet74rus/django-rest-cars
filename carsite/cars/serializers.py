import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Cars

class CarsModel:
    def __init__(self, title, description):
        self.title = title
        self.description = description

class CarsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()

def encode():
    model = CarsModel('Mercedes-Benz C180', 'description: C180')
    model_sr = CarsSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)

def decode():
    stream = io.BytesIO(b'{"title": "Mercedes-Benz C180", "description": "description: C180"}')
    data = JSONParser().parse(stream)
    serializer = CarsSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
from rest_framework import serializers
from .models import ElevatorSystem, Elevator

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = '__all__'

class ElevatorSystemSerializer(serializers.ModelSerializer):
    elevators = ElevatorSerializer(many=True)

    class Meta:
        model = ElevatorSystem
        fields = '__all__'

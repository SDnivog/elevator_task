from rest_framework import generics
from .models import ElevatorSystem, Elevator
from .serializers import ElevatorSerializer,ElevatorSystemSerializer

class ElevatorListCreateView(generics.ListCreateAPIView):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

class ElevatorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

class ElevatorSystemInitializeView(generics.CreateAPIView):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

class ElevatorSystemRequestsView(generics.ListCreateAPIView):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

class ElevatorSystemNextDestinationFloorView(generics.RetrieveAPIView):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

class ElevatorSystemIsMovingUpOrDownView(generics.RetrieveAPIView):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

class ElevatorSystemIsOperationalView(generics.UpdateAPIView):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

class ElevatorSystemOpenDoorView(generics.UpdateAPIView):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

class ElevatorSystemCloseDoorView(generics.UpdateAPIView):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

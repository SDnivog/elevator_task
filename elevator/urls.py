from django.urls import path
from .views import (
    ElevatorListCreateView,
    ElevatorRetrieveUpdateDestroyView,
    ElevatorSystemInitializeView,
    ElevatorSystemRequestsView,
    ElevatorSystemNextDestinationFloorView,
    ElevatorSystemIsMovingUpOrDownView,
    ElevatorSystemIsOperationalView,
    ElevatorSystemOpenDoorView,
    ElevatorSystemCloseDoorView,
)

urlpatterns = [
    path('elevators/', ElevatorListCreateView.as_view(), name='elevator-list-create'),
    path('elevators/<int:pk>/', ElevatorRetrieveUpdateDestroyView.as_view(), name='elevator-retrieve-update-destroy'),
    path('elevator-system/initialise/', ElevatorSystemInitializeView.as_view(), name='elevator-system-initialize'),
    path('elevator-system/<int:elevator_id>/requests/', ElevatorSystemRequestsView.as_view(), name='elevator-system-requests'),
    path('elevator-system/<int:elevator_id>/next-destination-floor/', ElevatorSystemNextDestinationFloorView.as_view(), name='elevator-system-next-destination-floor'),
    path('elevator-system/<int:elevator_id>/is-moving-up-or-down/', ElevatorSystemIsMovingUpOrDownView.as_view(), name='elevator-system-is-moving-up-or-down'),
    path('elevator-system/<int:elevator_id>/is-operational/', ElevatorSystemIsOperationalView.as_view(), name='elevator-system-is-operational'),
    path('elevator-system/<int:elevator_id>/open-door/', ElevatorSystemOpenDoorView.as_view(), name='elevator-system-open-door'),
    path('elevator-system/<int:elevator_id>/close-door/', ElevatorSystemCloseDoorView.as_view(), name='elevator-system-close-door'),
]

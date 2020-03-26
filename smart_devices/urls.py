from django.urls import path
from smart_devices.views import *


urlpatterns = [
    path('room', RoomView.as_view(), name='home'),
    path('room/<int:pk>', RoomDetailView.as_view(), name='room_detail'),
    path('add_room', AddRoomView.as_view(), name='add_room'),
]

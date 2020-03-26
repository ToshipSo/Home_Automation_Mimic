from django.urls import path
from django.views.generic import RedirectView

from smart_devices.views import *

urlpatterns = [
    path('', RedirectView.as_view(url='/login'), name='redirect_to_login'),
    path('rooms', RoomView.as_view(), name='home'),
    path('devices', RoomDetailView.as_view(), name='room_detail'),
    path('add_room', AddRoomView.as_view(), name='add_room'),
    path('add_device', AddDeviceView.as_view(), name='add_device'),
    path('device_control', DeviceControlAPI.as_view(), name='devices'),
    path('delete_room', DeleteRoomAPI.as_view(), name='delete_room'),
    path('delete_device', DeleteDeviceAPI.as_view(), name='delete_device'),
]

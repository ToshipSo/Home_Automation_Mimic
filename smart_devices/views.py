from django.views.generic import CreateView, ListView
from rest_framework.response import Response
from rest_framework.views import APIView

from smart_devices.forms import AddRoomForm
from smart_devices.models import *
from smart_devices.serializers import *


# Create your views here.
class RoomView(ListView):
    queryset = Room.objects.all()
    template_name = 'home.html'
    context_object_name = 'rooms'


class AddRoomView(CreateView):
    form_class = AddRoomForm
    template_name = 'add_form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        ctx = super(AddRoomView, self).get_context_data(**kwargs)
        ctx['form_name'] = 'Add Room'
        return ctx


class RoomDetailView(ListView):
    template_name = 'room_detail.html'
    context_object_name = 'devices'

    def get_queryset(self):
        devices = Device.objects.filter(room=self.kwargs['pk'])
        return devices


class DeviceControlAPI(APIView):
    def put(self, request):
        device = Device.objects.get(pk=request.data['pk'])
        device_type_instance = getattr(device, device.type.lower())
        del request.data['pk']
        serializer = None
        if device.type == device.LIGHT:
            serializer = LightSerializer(device_type_instance, data=request.data, partial=True)
        elif device.type == device.FAN:
            serializer = FanSerializer(device_type_instance, data=request.data, partial=True)
        elif device.type == device.AC:
            serializer = ACSerializer(device_type_instance, data=request.data, partial=True)
        elif device.type == device.TV:
            serializer = TVSerializer(device_type_instance, data=request.data, partial=True)
        elif device.type == device.LOCK:
            serializer = LockSerializer(device_type_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



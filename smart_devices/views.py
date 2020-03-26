from django.views.generic import CreateView, ListView
from rest_framework.response import Response
from rest_framework.views import APIView

from smart_devices.forms import *
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
    success_url = '/rooms'

    def get_context_data(self, **kwargs):
        ctx = super(AddRoomView, self).get_context_data(**kwargs)
        ctx['form_name'] = 'Add Room'
        return ctx


class AddDeviceView(CreateView):
    form_class = AddDeviceForm
    template_name = 'add_form.html'
    success_url = '/rooms'


class RoomDetailView(ListView):
    template_name = 'room_detail.html'
    context_object_name = 'devices'

    def get_queryset(self):
        room_id = self.request.GET.get('room', None)
        devices = Device.objects.all()
        if room_id:
            devices = devices.filter(room=room_id)
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


class DeleteRoomAPI(APIView):
    def delete(self, request):
        room = Room.objects.filter(pk=request.data['pk']).delete()
        if room[0] != request.data['pk']:
            return Response({
                'Status': 'Could not find room {0}'.format(request.data['pk'])
            })
        return Response({
            'Status': 'Room {0} deleted successfully'.format(request.data['pk'])
        })


class DeleteDeviceAPI(APIView):
    def delete(self, request):
        device = Device.objects.filter(pk=request.data['pk']).delete()
        if device[0] != request.data['pk']:
            return Response({
                'Status': 'Could not find device {0}'.format(request.data['pk'])
            })
        return Response({
            'Status': 'Device {0} deleted successfully'.format(request.data['pk'])
        })

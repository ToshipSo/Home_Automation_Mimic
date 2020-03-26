from django.views.generic import CreateView, ListView
from smart_devices.models import *
from smart_devices.forms import AddRoomForm


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

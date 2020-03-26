from django.forms import ModelForm
from smart_devices.models import Room


class AddRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

from django.forms import ModelForm

from smart_devices.models import *


class AddRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class AddDeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = '__all__'

    def save(self, commit=True):
        device = super(AddDeviceForm, self).save(commit=False)
        if commit:
            device.save()
            if device.type == device.LIGHT:
                Light.objects.create(device=device, brightness=Light.MIN_BRIGHTNESS)
            elif device.type == device.FAN:
                Fan.objects.create(device=device, speed=Fan.MIN_SPEED)
            elif device.type == device.AC:
                AC.objects.create(device=device, temperature=AC.MIN_TEMP, mode=AC.AUTO)
            elif device.type == device.TV:
                TV.objects.create(device=device, volume=TV.MIN_VOL, input=TV.HDMI1)
            elif device.type == device.LOCK:
                Lock.objects.create(device=device)
        return device

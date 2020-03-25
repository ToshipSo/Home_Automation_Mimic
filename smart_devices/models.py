from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Room(models.Model):
    HALL = 'HALL'
    KITCHEN = 'KITCHEN'
    BEDROOM = 'BEDROOM'
    ROOM_TYPE = (
        (HALL, 'Hall'),
        (KITCHEN, 'Kitchen'),
        (BEDROOM, 'Bedroom')
    )
    room_name = models.CharField(max_length=20)
    room_type = models.CharField(max_length=15, choices=ROOM_TYPE, default=BEDROOM)

    def __str__(self):
        return self.room_name


class Device(models.Model):
    AC = 'AC'
    TV = 'TV'
    LIGHT = 'LIGHT'
    FAN = 'FAN'
    LOCK = 'LOCK'
    ALARM = 'ALARM'
    STATUS_ON = True
    STATUS_OFF = False
    DEVICE_TYPE = (
        (AC, 'AC'),
        (TV, 'TV'),
        (LIGHT, 'Light'),
        (FAN, 'Fan'),
        (LOCK, 'Lock'),
        (ALARM, 'Alarm')
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=DEVICE_TYPE)

    def __str__(self):
        return '{0} {1}'.format(self.room.room_name, self.name)


class Light(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    brightness = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.device.room.room_name + ' ' + self.device.name


class Fan(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    speed = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.device.room.room_name + ' ' + self.device.name


class AC(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    temperature = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(40)])

    def __str__(self):
        return self.device.room.room_name + ' ' + self.device.name


class TV(models.Model):
    HDMI1 = 'HDMI1'
    HDMI2 = 'HDMI2'
    AV = 'AV'
    PRIME = 'PRIME'
    NETFLIX = 'NETFLIX'
    INPUT_TYPE = (
        (HDMI1, 'HDMI 1'),
        (HDMI2, 'HDMI 2'),
        (AV, 'AV'),
        (PRIME, 'Amazon Prime'),
        (NETFLIX, 'Netflix')
    )
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    volume = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    input = models.CharField(max_length=15, choices=INPUT_TYPE, default=HDMI1)

    def __str__(self):
        return self.device.room.room_name + ' ' + self.device.name


class Lock(models.Model):
    ARMED = True
    UNARMED = False
    SECURITY_OPTIONS = (
        (ARMED, 'Armed'),
        (UNARMED, 'Unarmed')
    )
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    status = models.BooleanField(choices=SECURITY_OPTIONS)

    def __str__(self):
        return self.device.room.room_name + ' ' + self.device.name

from django.contrib import admin

from smart_devices.models import *

# Register your models here.
admin.site.register(Room)
admin.site.register(Device)
admin.site.register(Light)
admin.site.register(Fan)
admin.site.register(TV)
admin.site.register(AC)
admin.site.register(Lock)

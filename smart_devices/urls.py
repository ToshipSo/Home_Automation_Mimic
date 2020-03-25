from django.urls import path
from smart_devices.views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
]

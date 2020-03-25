from django.shortcuts import render
from django.views.generic import View, ListView
from smart_devices.models import *


# Create your views here.
class Home(ListView):
    queryset = Room.objects.all()
    template_name = 'home.html'
    context_object_name = 'rooms'

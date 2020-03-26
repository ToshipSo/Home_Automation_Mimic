from rest_framework.serializers import ModelSerializer

from smart_devices.models import Fan, Light, AC, TV, Lock


class FanSerializer(ModelSerializer):
    class Meta:
        model = Fan
        fields = '__all__'


class LightSerializer(ModelSerializer):
    class Meta:
        model = Light
        fields = '__all__'


class ACSerializer(ModelSerializer):
    class Meta:
        model = AC
        fields = '__all__'


class TVSerializer(ModelSerializer):
    class Meta:
        model = TV
        fields = '__all__'


class LockSerializer(ModelSerializer):
    class Meta:
        model = Lock
        fields = '__all__'

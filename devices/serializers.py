from rest_framework import serializers

from devices.models import Device


class SerDeviceDetail(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class SerDeviceList(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
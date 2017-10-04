from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from devices.models import Device
from devices.serializers import SerDeviceList, SerDeviceDetail


class DeviceList(APIView):

    def get(self, request, format=None):
        returndata = [['ID', 'Name', 'Diameter', 'Height']]
        temparray = []
        device = Device.objects.all()
        serializer = SerDeviceList(device, many=True)
        for content in serializer.data:
            for k, v in content.items():
                temparray.append(v)
            returndata.append(temparray)
            temparray = []
        return Response(returndata)


class DeviceDetail(APIView):

    def get_object(self, pk):
        try:
            return Device.objects.get(pk=pk)
        except Device.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SerDeviceDetail(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tank = Device.objects.get(pk=pk)
        serializer = SerDeviceDetail(tank, data=request.data["payload"])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


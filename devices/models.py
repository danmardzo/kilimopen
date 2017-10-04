from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
from devices import defaults


class Device(models.Model):
    name = models.CharField(max_length=100, unique=True)
    devicelink = models.ForeignKey('DeviceLink', related_name='slave_device', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        ordering = ('name', )
        verbose_name_plural = "Devices"


class Observation(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=50)
    device = models.ForeignKey(Device, related_name='device_obsrv')


class Status(models.Model):
    is_on = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, related_name='device_state')

    class Meta:
        ordering = ('timestamp', )
        verbose_name_plural = "Status"


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, default='interger')
    value_int = models.IntegerField(null=True, default=0, blank=True)
    value_char = models.IntegerField(null=True, default='', blank=True)
    units = models.CharField(max_length=50, null=True, default='', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, related_name='device_attr')


class DeviceLink(models.Model):
    name = models.CharField(max_length=100)
    device = models.ForeignKey(Device, related_name='linked_device', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '%s' % self.name

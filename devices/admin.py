from django.contrib import admin

# Register your models here.
from devices.models import Device, Attribute, Status, DeviceLink, Observation


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name',)

admin.site.register(Device, DeviceAdmin)


class ObservationAdmin(admin.ModelAdmin):
    list_display = ('get_device', )

    def get_device(self, obj):
        return obj.device.name

admin.site.register(Observation, ObservationAdmin)


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name',)

admin.site.register(Attribute, AttributeAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('get_device', )

    def get_device(self, obj):
        return obj.device.name

admin.site.register(Status, StatusAdmin)


class DeviceLinkAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name',)

admin.site.register(DeviceLink, DeviceLinkAdmin)

admin.site.site_header = 'openKILIMO'
admin.site.index_title = 'Admin Dashboard'

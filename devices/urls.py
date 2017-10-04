from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from devices import views

urlpatterns = [
    url(r'^model/devices/(?P<pk>[0-9]+)/$', views.DeviceDetail.as_view()),
    url(r'^model/devices/$', views.DeviceList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
admin.site.site_title = 'Admin Dashboard'


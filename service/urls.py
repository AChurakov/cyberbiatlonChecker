from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/(?P<method_name>\w+)/$', views.api, name='api'),
]
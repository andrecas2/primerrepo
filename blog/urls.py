from django.conf.urls import include, url
from . import views
from django.utils import timezone

urlpatterns = [
    url(r'^$', views.listado),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detalle, name='detalle'),
    
]

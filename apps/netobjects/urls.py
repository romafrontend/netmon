from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'corenetworkobjects/$', views.corenetworkobject, name='corenetworkobjects'),
]

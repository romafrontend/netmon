from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'firewalls/$', views.firewalls, name='firewalls'),
    url(r'routers/$', views.routers, name='routers')
]
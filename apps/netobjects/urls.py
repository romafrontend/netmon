from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'json_corenetworkobjects/$', views.json_corenetworkobjects, name='json_corenetworkobjects'),
    url(r'corenetworkobjects/$', views.corenetworkobjects, name='corenetworkobjects'),
]

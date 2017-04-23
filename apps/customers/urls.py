from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'companies/$', views.companies, name='companies'),
    url(r'sites/$', views.sites, name='sites')
]

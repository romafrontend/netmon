from django.shortcuts import render

from .models import Firewall, Router

# Create your views here.


def firewalls(request):
    firewalls_list = Firewall.objects.all()
    context = {'firewalls_list': firewalls_list}
    return render(request, 'firewalls.html', context)


def routers(request):
    routers_list = Router.objects.all()
    context = {'routers_list': routers_list}
    return render(request, 'routers.html', context)

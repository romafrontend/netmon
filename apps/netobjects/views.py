from django.shortcuts import render

from .models import CoreNetworkObject

# Create your views here.


def corenetworkobject(request):
    corenetworkobjects_list = CoreNetworkObject.objects.all()
    context = {'corenetworkobjects_list': corenetworkobjects_list}
    return render(request, 'corenetworkobjects.html', context)

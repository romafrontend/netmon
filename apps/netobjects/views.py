import json

from django.shortcuts import render
from django.core import serializers

from .models import CoreNetworkObject


def corenetworkobjects(request):
    corenetworkobjects_list = CoreNetworkObject.objects.all()
    context = {'corenetworkobjects_list': corenetworkobjects_list}
    return render(request, 'corenetworkobjects.html', context)


def json_corenetworkobjects(request):
    qs = CoreNetworkObject.objects.values('id', 'cli_address', 'web_address')
    # my_json = serializers.serialize("json", qs)
    my_json = json.dumps({'table': list(qs)})
    context = {'my_json': my_json}
    return render(request, 'index.html', context)

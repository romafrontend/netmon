from django.shortcuts import render

from .models import Company, Site

# Create your views here.


def companies(request):
    companies_list = Company.objects.all()
    context = {'companies_list': companies_list}
    return render(request, 'companies.html', context)


def sites(request):
    sites_list = Site.objects.all()
    context = {'sites_list': sites_list}
    return render(request, 'sites.html', context)

from django.contrib import admin

# Register your models here.
from .models import Company, Site


class CompanyAdmin(admin.ModelAdmin):
    fields = ['name']


class SiteAdmin(admin.ModelAdmin):
    fields = ['name', 'company_name']
    list_display = ('name', 'company_name')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Site, SiteAdmin)

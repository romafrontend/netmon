from django.contrib import admin

# Register your models here.
from .models import Company, Site


class CompanyAdmin(admin.ModelAdmin):
    fields = ['name', 'company_type']


class SiteAdmin(admin.ModelAdmin):
    fields = ['company_name', 'name']
    list_display = ('company_name', 'name')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Site, SiteAdmin)

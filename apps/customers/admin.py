from django.contrib import admin

# Register your models here.
from .models import Company, Site


class SiteAdmin(admin.ModelAdmin):
    fields = ['company_name', 'name']
    list_display = ('company_name', 'name')


admin.site.register(Company)
admin.site.register(Site, SiteAdmin)

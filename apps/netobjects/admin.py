from django.contrib import admin

# Register your models here.
from .models import BluePrintNetworkObject, CoreNetworkObject


class CoreNetworkObjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('IP Details',          {'fields': ['web_address', 'cli_access_port']}),
        ('Access Credentials',  {'fields': ['login', 'password']}),
        ('Common Details',      {'fields': ['site_name', 'spec_model']}),
        ('Auto Fulfill Fields', {'fields': ['cli_address', 'ipv4_external_address', 'dns_address']})
    ]
    list_display = ['site_name', 'spec_model', 'web_address', 'cli_address', 'login', 'password']


admin.site.register(BluePrintNetworkObject)
admin.site.register(CoreNetworkObject, CoreNetworkObjectAdmin)
 
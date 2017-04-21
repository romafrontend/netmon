from django.contrib import admin

# Register your models here.
from .models import BluePrintNetworkObject, Firewall, Router


class FirewallAdmin(admin.ModelAdmin):
    fieldsets = [
        ('IP Details',          {'fields': ['web_address', 'cli_access_port']}),
        ('Access Credentials',  {'fields': ['login', 'password']}),
        ('Common Details',      {'fields': ['site_name', 'spec_model']}),
    ]
    list_display = ['site_name', 'spec_model', 'web_address', 'login', 'password']


admin.site.register(BluePrintNetworkObject)
admin.site.register(Firewall, FirewallAdmin)
admin.site.register(Router, FirewallAdmin)

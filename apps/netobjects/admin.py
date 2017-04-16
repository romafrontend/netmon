from django.contrib import admin

# Register your models here.
from .models import Firewall


class FirewallAdmin(admin.ModelAdmin):
    fieldsets = [
        ('IP Details',          {'fields': [
            'web_address', 'cli_access_port',
            'cli_address', 'ipv4_external_address',
            'web_access_port'
        ]}),
        ('Access Credentials',  {'fields': ['login', 'password']}),
        (None,                  {'fields': ['site_name']}),
    ]
    list_display = ['site_name', 'web_address', 'cli_address', 'login', 'password']


admin.site.register(Firewall, FirewallAdmin)

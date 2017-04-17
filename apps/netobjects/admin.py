from django.contrib import admin

# Register your models here.
from .models import Firewall, Router


class FirewallAdmin(admin.ModelAdmin):
    fieldsets = [
        ('IP Details',          {'fields': [
            'web_address', 'cli_access_port', 'dns_address',
            'cli_address', 'ipv4_external_address',
        ]}),
        ('Access Credentials',  {'fields': ['login', 'password']}),
        ('Common Details',      {'fields': ['site_name', 'manufacturer', 'model_version']}),
    ]
    list_display = ['site_name', 'web_address', 'cli_address', 'login', 'password']


class RouterAdmin(admin.ModelAdmin):
    fieldsets = FirewallAdmin.fieldsets
    list_display = FirewallAdmin.list_display


admin.site.register(Firewall, FirewallAdmin)
admin.site.register(Router, RouterAdmin)

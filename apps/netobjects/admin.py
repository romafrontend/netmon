from django.contrib import admin

# Register your models here.
from .models import Firewall


class FirewallAdmin(admin.ModelAdmin):
    fieldsets = [
        ('IP Details',          {'fields': ['ipv4_address', 'port']}),
        ('Access Credentials',  {'fields': ['login', 'password']}),
        (None,                  {'fields': ['site_name']}),
    ]
    list_display = ['site_name', 'ipv4_address', 'port', 'login', 'password']


admin.site.register(Firewall, FirewallAdmin)

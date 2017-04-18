from django.contrib import admin

# Register your models here.
from .models import Firewall, Router


class FirewallAdmin(admin.ModelAdmin):
    fieldsets = [
        ('IP Details',          {'fields': ['web_address', 'cli_access_port']}),
        ('Access Credentials',  {'fields': ['login', 'password']}),
        ('Common Details',      {'fields': ['site_name', 'manufacturer', 'model_version']}),
    ]
    list_display = ['site_name', 'web_address', 'login', 'password']


class RouterAdmin(admin.ModelAdmin):
    fieldsets = FirewallAdmin.fieldsets
    list_display = FirewallAdmin.list_display


admin.site.register(Firewall, FirewallAdmin)
admin.site.register(Router, RouterAdmin)

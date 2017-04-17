from django.contrib import admin

# Register your models here.
from .models import BackupFirewall, BackupRouter


class BackupFirewallAdmin(admin.ModelAdmin):
    fields = ['site_name', 'object_backup', 'time_interval', 'file_location']
    list_display = ['site_name', 'object_backup', 'time_interval', 'file_location']


class BackupRouterAdmin(admin.ModelAdmin):
    fields = BackupFirewallAdmin.fields
    list_display = BackupFirewallAdmin.list_display


admin.site.register(BackupFirewall, BackupFirewallAdmin)
admin.site.register(BackupRouter, BackupRouterAdmin)

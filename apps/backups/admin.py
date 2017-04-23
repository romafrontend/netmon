from django.contrib import admin

# Register your models here.
from .models import BackupFirewall, BackupRouter


class BackupFirewallAdmin(admin.ModelAdmin):
    fields = ['object_backup', 'time_interval']
    list_display = ['object_backup', 'time_interval']


class BackupRouterAdmin(admin.ModelAdmin):
    fields = BackupFirewallAdmin.fields
    list_display = BackupFirewallAdmin.list_display


admin.site.register(BackupFirewall, BackupFirewallAdmin)
admin.site.register(BackupRouter, BackupRouterAdmin)

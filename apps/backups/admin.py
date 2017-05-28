from django.contrib import admin

# Register your models here.
from .models import CoreBackup


class CoreBackupAdmin(admin.ModelAdmin):
    list_display = ['object_backup', 'site_name']

    # that func allow us to use subfield from the ForeignKey
    def site_name(self, obj):
        return obj.object_backup.site_name


admin.site.register(CoreBackup, CoreBackupAdmin)

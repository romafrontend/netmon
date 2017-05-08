from django.contrib import admin

# Register your models here.
from .models import CoreBackup


class CoreBackupAdmin(admin.ModelAdmin):
    list_display = ['object_backup', 'time_interval']


admin.site.register(CoreBackup, CoreBackupAdmin)

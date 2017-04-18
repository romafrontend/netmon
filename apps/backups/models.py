from django.db import models

from apps.core.models import TimeStampedModel
from apps.netobjects.models import Firewall, Router

# Create your models here.


class CoreBackup(TimeStampedModel):
    object_backup = 'that line I need only for compatability'  # <-- !!!!
    time_interval = models.IntegerField(default=1)
    file_location = models.CharField(max_length=255)

    # fields that suppose to be fullfilled automatically
    site_name = models.CharField(max_length=64, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.object_backup)

    def save(self, *args, **kwargs):
        if not self.site_name:  # automatically fullfill site_name field only if it is empty
            self.site_name = self.object_backup.site_name.company_name.name + ' ' + self.object_backup.site_name.name
        super().save(*args, **kwargs)  # finally call for normal save method


class BackupFirewall(CoreBackup):
    object_backup = models.ForeignKey(Firewall, on_delete=models.CASCADE)


class BackupRouter(CoreBackup):
    object_backup = models.ForeignKey(Router, on_delete=models.CASCADE)

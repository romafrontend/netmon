from django.db import models

from apps.core.models import TimeStampedModel
from apps.netobjects.models import Firewall, Router
from apps.customers.models import Site

# Create your models here.


class CoreBackup(TimeStampedModel):
    object_backup = 'that line I need only for compatability'  # <-- !!!!
    site_name = models.ForeignKey(Site)
    time_interval = models.IntegerField(default=1)
    file_location = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.object_backup)


class BackupFirewall(CoreBackup):
    object_backup = models.ForeignKey(Firewall)


class BackupRouter(CoreBackup):
    object_backup = models.ForeignKey(Router)

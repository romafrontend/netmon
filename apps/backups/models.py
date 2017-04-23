from django.db import models

from apps.core.models import TimeStampedModel
from apps.netobjects.models import Firewall, Router

# Create your models here.


class CoreBackup(TimeStampedModel):
    object_backup = 'that line need only for compatability'  # <-- !!!!
    time_interval = models.IntegerField(default=1)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.object_backup)


class BackupFirewall(CoreBackup):
    object_backup = models.ForeignKey(Firewall, on_delete=models.CASCADE)


class BackupRouter(CoreBackup):
    object_backup = models.ForeignKey(Router, on_delete=models.CASCADE)

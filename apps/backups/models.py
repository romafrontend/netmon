from django.db import models

from apps.core.models import TimeStampedModel
from apps.netobjects.models import CoreNetworkObject
from .tasks import fortigate_backup


class CoreBackup(TimeStampedModel):
    object_backup = models.ForeignKey(CoreNetworkObject, on_delete=models.CASCADE)
    time_interval = models.IntegerField(default=1)
    last_backup_status = models.TextField(blank=True)

    def __str__(self):
        return str(self.object_backup)

    def save(self, *args, **kwargs):
        # call for normal save method first of all, I can't activate scripts on object that still not exist(saved)
        super().save(*args, **kwargs)

        if self.object_backup.spec_model.model_family == 'FortiGate':  # check that we backup FortiNet device
            # we need countdown, because otherwise Django don't have enough time to create new object in database
            command, log = fortigate_backup.s(self.id).apply_async(countdown=3)
            self.last_backup_status = log

            # again we 'save' because we need to update and save last_backup_status field
            super().save(*args, **kwargs)

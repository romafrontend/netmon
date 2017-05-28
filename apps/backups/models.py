from django.db import models

from apps.core.models import TimeStampedModel
from apps.netobjects.models import CoreNetworkObject
from .tasks import device_backup


class CoreBackup(TimeStampedModel):
    object_backup = models.ForeignKey(CoreNetworkObject, on_delete=models.CASCADE)
    time_interval = models.IntegerField(default=1)
    last_backup_status = models.TextField(blank=True)

    def __str__(self):
        return str(self.object_backup)

    def save(self, *args, **kwargs):
        # call for normal save method first of all, I can't activate scripts on object that still not exist(saved)
        super().save(*args, **kwargs)

        # for example if company is Hewlett Packard, then company_name = hewlett_packard
        corp_folder = self.object_backup.site_name.company_name.name.replace(" ", "_").lower()
        site_folder = self.object_backup.site_name.name.replace(" ", "_").lower()
        device_folder = CoreBackup.__str__(self).replace(" ", "_").lower()

        if 'FortiGate' or 'Cisco' in CoreBackup.__str__(self):  # check that we backup FortiGate device
            # we need countdown, because otherwise Django don't have enough time to create new object in database
            log = device_backup.s(corp_folder, site_folder, device_folder, self.id).apply_async(countdown=3)

        # again we 'save' because we need to update and save last_backup_status field
        self.last_backup_status = log
        super().save(*args, **kwargs)

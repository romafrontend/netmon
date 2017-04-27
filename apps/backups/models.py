from django.db import models

from apps.core.models import TimeStampedModel
from apps.netobjects.models import CoreNetworkObject

# Create your models here.


class CoreBackup(TimeStampedModel):
    object_backup = models.ForeignKey(CoreNetworkObject, on_delete=models.CASCADE)
    time_interval = models.IntegerField(default=1)

    def __str__(self):
        return str(self.object_backup)

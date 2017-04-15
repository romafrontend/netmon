from django.db import models

from apps.core.models import TimeStampedModel
from apps.customers.models import Site
# Create your models here.


class Firewall(TimeStampedModel):
    ipv4_address = models.GenericIPAddressField()
    port = models.IntegerField(default=None, null=True)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    site_name = models.ForeignKey(Site)

    def __str__(self):
        return str(self.site_name)

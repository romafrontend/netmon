from django.db import models

from apps.core.models import TimeStampedModel
from apps.customers.models import Site
# Create your models here.


class Firewall(TimeStampedModel):
    # data that we add manually
    web_address = models.CharField(max_length=29, null=True)  # https:// + 255.255.255.255 + :65550
    cli_access_port = models.IntegerField(default=22, null=True)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    site_name = models.ForeignKey(Site)

    # fields that suppose to be fullfilled automatically
    cli_address = models.CharField(max_length=21, blank=True)  # 255.255.255.255 + :65550
    ipv4_external_address = models.GenericIPAddressField(blank=True, null=True)
    web_access_port = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.site_name)

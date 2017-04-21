from django.db import models

import re  # module for searches

from apps.core.models import TimeStampedModel
from apps.customers.models import Company, Site

from .choices import OBJECT_TYPE
# Create your models here.


class BluePrintNetworkObject(TimeStampedModel):
    ''' here we add only tech specifications of device, that we take from manufacturer site.
    Like number of ports and cpu. We don't add nothing like web_address,
    only attributes that we took from tech specification '''
    object_type = models.CharField(max_length=2, choices=OBJECT_TYPE)
    model_family = models.CharField(max_length=20, verbose_name='Family')
    model_version = models.CharField(max_length=20, verbose_name='Model')
    company_name = models.ForeignKey(Company, null=True)

    def __str__(self):
        return self.model_family + ' ' + self.model_version


class CoreNetworkObject(TimeStampedModel):
    ''' everything bellow we use to create other network objects with common attributes, like firewalls and routers '''
    # data that we add manually
    web_address = models.CharField(max_length=100, default='https://')  # https:// + 255.255.255.255 + :65550
    cli_access_port = models.IntegerField(default=22)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    site_name = models.ForeignKey(Site)
    spec_model = models.ForeignKey(BluePrintNetworkObject)

    # fields that suppose to be fullfilled automatically, I even do not permit to edit them
    cli_address = models.CharField(max_length=255, blank=True, editable=False)  # 1.1.1.1:22 or blala.dyndns.org:22
    ipv4_external_address = models.CharField(max_length=255, blank=True, editable=False)  # 255.255.255.255
    dns_address = models.CharField(max_length=255, blank=True, editable=False)  # blablabla.dyndns.org

    class Meta:
        abstract = True

    def pattern_web_address(self):
        '''First we create/find pattern of one key field, and then use it to autofill another fields'''
        # https://1.1.1.1 or https://1.1.1.1:443
        pattern_web_address = re.match('(^\w+):1//(\d+.\d+.\d+.\d+)', self.web_address)
        dns_check = False  # flag, that show that web_address is IP address or DNS address, by defailt it's IP address
        if not pattern_web_address:
            pattern_web_address = re.match('(^\w+)://(.+):(\d+)', self.web_address)  # https://blabla.dyndns.org:65550
            dns_check = True
        if not pattern_web_address:
            pattern_web_address = re.match('(^\w+)://(.+)', self.web_address)  # https://blablabla.dyndns.org
            dns_check = True
        # automatically fullfill cli_address, dns_address/ipv4_external_address fields only if they are empty,
        # and we found pattern_web_address
        if pattern_web_address:
            if not self.cli_address:
                self.cli_address = pattern_web_address.group(2) + ':' + str(self.cli_access_port)
            if dns_check:  # fullfill only 1 of 2 fields: or dns or ipv4
                if not self.dns_address:
                    self.dns_address = pattern_web_address.group(2)
            else:
                if not self.ipv4_external_address:
                    self.ipv4_external_address = pattern_web_address.group(2)

    def save(self, *args, **kwargs):
        CoreNetworkObject.pattern_web_address(self)
        super().save(*args, **kwargs)  # finally call for normal save method

    def __str__(self):
        return str(self.spec_model)


class Firewall(CoreNetworkObject):
    # that field we need only for other models to identify what they are working with
    object_type = models.CharField(max_length=32, default='firewall', editable=False)


class Router(CoreNetworkObject):
    object_type = models.CharField(max_length=32, default='router', editable=False)

from django.db import models

import re  # module for searches

from apps.core.models import TimeStampedModel
from apps.customers.models import Company, Site

from .choices import OBJECT_TYPE
# Create your models here.


class BluePrintNetworkObject(TimeStampedModel):
    ''' here we add only tech specifications of device, that we take from manufacturer site.
    Like number of ports and cpu. We don't add nothing like web_address '''
    object_type = models.CharField(max_length=2, choices=OBJECT_TYPE)
    model_family = models.CharField(max_length=20, verbose_name='Family')
    model_version = models.CharField(max_length=20, verbose_name='Model')
    company_name = models.ForeignKey(Company, null=True)

    def __str__(self):
        return self.model_family + ' ' + self.model_version


class CoreNetworkObject(TimeStampedModel):
    ''' Everything bellow we use to create other network objects with common attributes,
    like firewalls and routers. Here we add fields only that unique for each device,
    like web address or login/pass. Exception is site_name and spec_model,
    we need those field to put objects in groups '''
    # data that we add manually
    web_address = models.CharField(max_length=100, default='https://')  # https:// + 255.255.255.255 + :65550
    cli_access_port = models.IntegerField(default=22)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    site_name = models.ForeignKey(Site)
    spec_model = models.ForeignKey(BluePrintNetworkObject)

    # fields that suppose to be fullfilled automatically, I even do not permit to edit them
    cli_address = models.CharField(max_length=255, blank=True)  # 1.1.1.1:22 or blala.dyndns.org:22
    ipv4_external_address = models.CharField(max_length=255, blank=True)  # 255.255.255.255
    dns_address = models.CharField(max_length=255, blank=True)  # blablabla.dyndns.org

    def pattern_web_address(self):
        '''First we create/find pattern of one key field, and then use it to autofill another fields'''
        # https://1.1.1.1 or https://1.1.1.1:443
        pattern_web_address = re.match('(^\w+)://(\d+.\d+.\d+.\d+)', self.web_address)
        # flag, that show that web_address is IP address or DNS address, 'False' means that by defailt it's IP address
        dns_check = False

        if not pattern_web_address:
            pattern_web_address = re.match('(^\w+)://(.+):(\d+)', self.web_address)  # https://blabla.dyndns.org:65550
            dns_check = True
            if not pattern_web_address:
                pattern_web_address = re.match('(^\w+)://(.+)', self.web_address)  # https://blablabla.dyndns.org
                dns_check = True

        # automatically fullfill cli_address, dns_address/ipv4_external_address fields
        self.cli_address = pattern_web_address.group(2) + ':' + str(self.cli_access_port)
        if dns_check:  # fullfill only 1 of 2 fields: or dns or ipv4
            self.dns_address = pattern_web_address.group(2)
            self.ipv4_external_address = ""
        else:
            self.ipv4_external_address = pattern_web_address.group(2)
            self.dns_address = ""

    def save(self, *args, **kwargs):
        CoreNetworkObject.pattern_web_address(self)
        super().save(*args, **kwargs)  # finally call for normal save method

    def __str__(self):
        return str(self.spec_model)

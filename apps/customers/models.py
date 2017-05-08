from django.db import models

from xkcdpass import xkcd_password as xp  # password generator module

from apps.core.models import TimeStampedModel
from .choices import COMPANY_TYPES
from .tasks import create_corp_user, create_site_folder_and_subfolders
# Create your models here.


class Company(TimeStampedModel):
    name = models.CharField(max_length=32, unique=True)
    company_type = models.CharField(
        max_length=2,
        choices=COMPANY_TYPES,
        verbose_name='Type'
    )

    # details for creation of new user on the server, that will serve as FTP and static storage
    ftp_password = models.CharField(max_length=32, verbose_name='FTP Password')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"

    def save(self, *args, **kwargs):
        # call for normal save method first of all, I can't activate scripts on object that still not exist(saved)
        super().save(*args, **kwargs)

        # we need countdown, because otherwise Django don't have enough time to create new object in database
        create_corp_user.s(self.name.lower(), self.ftp_password).apply_async(countdown=3)


class Site(TimeStampedModel):
    name = models.CharField(max_length=32)
    company_name = models.ForeignKey(Company)

    def __str__(self):
        return '%s %s' % (self.company_name, self.name)

    class Meta:
        ordering = ('company_name',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        create_site_folder_and_subfolders.s(self.id).apply_async(countdown=3)

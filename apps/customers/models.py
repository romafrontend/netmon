from django.db import models

from apps.core.models import TimeStampedModel
from .dropdown_options import COMPANY_TYPES
from .tasks import create_site_folder_and_subfolders
# Create your models here.


class Company(TimeStampedModel):
    name = models.CharField(max_length=32, unique=True)
    company_type = models.CharField(max_length=2, choices=COMPANY_TYPES, verbose_name='Type')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class Site(TimeStampedModel):
    name = models.CharField(max_length=32)
    company_name = models.ForeignKey(Company)

    def __str__(self):
        return '%s %s' % (self.company_name, self.name)

    class Meta:
        ordering = ('company_name',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # script bellow will create new folders in staticfiles/corp_folder/site_folder/subfolder
        corp_folder = self.company_name.name.replace(" ", "_").lower()
        site_folder = self.name.replace(" ", "_").lower()
        subfolders = ['backups', 'logs', 'documents']
        create_site_folder_and_subfolders.s(corp_folder, site_folder, *subfolders).apply_async(countdown=3)

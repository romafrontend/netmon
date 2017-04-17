from django.db import models

from apps.core.models import TimeStampedModel
# Create your models here.


class Company(TimeStampedModel):
    name = models.CharField(max_length=32)

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

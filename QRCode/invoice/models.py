from django.db import models
from django.utils import timezone

class Invoice(models.Model):
    fromCompany     = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, related_name='fromCompany',)
    toCompany       = models.ForeignKey('Company', on_delete=models.SET_NULL, blank=True, null=True, related_name='toCompany',)
    toCompanyName   = models.CharField(max_length=100, blank=True,)
    description     = models.CharField(max_length=100)
    date_created    = models.DateTimeField(default=timezone.now)
    # TODO change to date_payed?
    last_modified   = models.DateTimeField(auto_now=True)

    # TODO more fields / custom fields or seriazized blob for additional data

    def __str__(self):
        # TODO implement
        return "{0} to {1} on {2}".format(self.fromCompany.name, self.toCompany.name if self.toCompany else self.toCompanyName, self.date_created)

class Company(models.Model):
    name            = models.CharField(max_length=100)
    taxNumber       = models.CharField(max_length=50)
    # TODO change to choices
    country         = models.CharField(max_length=50)

    def __str__(self):
        return self.name
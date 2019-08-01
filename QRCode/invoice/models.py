from django.db import models
from django.utils import timezone

class Invoice(models.Model):
    FromCompany = models.CharField()
    ToCompany = models.CharField()
    txt = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    # TODO change to date_payed
    last_modified = models.DateTimeField(auto_now=True)
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

    """
    unique_invoice_id                = models.CharField(max_length = 255, primary_key = True)
    unique_user_id                   = models.ForeignKey('User')
    upload_timestamp
    invoice_hash
    order_number
    operation_date
    invoice_date
    invoice_number
    customer
    vat_number
    concept
    price
    quantity
    discount
    tax_base
    deductible_vat_percent
    deductible_vat
    equivalence_surcharge_percent
    equivalence_surcharge
    withholding_percent
    withholding
    total_invoice
    due_date
    payment_method
    bank_account
    address
    city
    postal_number
    """


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
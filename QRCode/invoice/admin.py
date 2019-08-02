from django.contrib import admin
from .models import Invoice, Company

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'fromCompany', 'toCompany', 'toCompanyName', 'description', 'date_created', 'last_modified']
    list_display_links = ['id']
    list_per_page = 25
    search_fields = ['id', 'fromCompany', 'toCompany', 'toCompanyName', 'description']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'taxNumber', 'country']
    list_display_links = ['id']
    list_per_page = 25
    search_fields = ['id', 'name', 'taxNumber', 'country']

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Company, CompanyAdmin)
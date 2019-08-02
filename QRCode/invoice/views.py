from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Invoice

def home(request):
    return render(request, 'invoice/home.html')

@login_required
def send(request):
    return render(request, 'invoice/send.html')

def view(request, invoice_id):
    # TODO custom 404 for invoice not found
    invoice = get_object_or_404(Invoice, pk=invoice_id)

    return render(request, 'invoice/view.html', {
        'invoice': invoice,
    })
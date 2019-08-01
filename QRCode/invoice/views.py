from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'invoice/home.html')

def send(request):
    return render(request, 'invoice/send.html')

def view(request, invoice_id):
    context = {
        "invoice_id": invoice_id
    }

    return render(request, 'invoice/view.html', context)
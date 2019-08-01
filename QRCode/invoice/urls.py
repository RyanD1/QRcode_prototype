from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='invoice-home'),
    path('send/', views.send, name='invoice-send'),
    # TODO: better regex
    path('view/<str:invoice_id>', views.view, name='invoice-view'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.upload, name='excelupload-home'),
    path('upload_failed', views.upload_failed, name='excelupload-failed'),
    path('upload_successful', views.upload_successful, name='excelupload-successful'),
]

from django.db import models
import hashlib

# Create your models here.


class ExcelFile(models.Model):
    excel = models.FileField(upload_to='excels/')
    uid = models.CharField(max_length=32, blank=False)
    file_hash = models.CharField(max_length=32, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.excel.delete()
        super().delete(*args, **kwargs)

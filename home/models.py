from django.db import models

class QRCode(models.Model):
    code_data = models.CharField(max_length=255)
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code_data

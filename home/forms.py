from django import forms
from .models import QRCode

class QRCodeForm(forms.ModelForm):
    class Meta:
        model = QRCode
        fields = ['code_data']

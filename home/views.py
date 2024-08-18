from django.shortcuts import render, redirect
from .models import QRCode
from .forms import QRCodeForm


def qr_code_scanner(request):
    if request.method == "POST":
        form = QRCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('qr_code_scanner')  # Replace 'success' with your desired redirect URL
    else:
        form = QRCodeForm()

    return render(request, 'qr_code_scanner.html', {'form': form})

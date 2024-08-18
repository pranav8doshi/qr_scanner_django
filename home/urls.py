from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.qr_code_scanner, name='qr_code_scanner'),

]

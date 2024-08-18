from django.urls import path
from . import views

urlpatterns = [
    path('', views.qr_code_scanner, name='qr_code_scanner'),

]

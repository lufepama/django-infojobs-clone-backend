from django.contrib import admin
from django.urls import path, include
from .views import create_email_code, get_email_code, verify_email_code

urlpatterns = [
    path('create-email-code/', create_email_code, name='create-email-codes'),
    path('get-email-code/<str:email>/', get_email_code, name='get-email-codes'),
    path('verify-email-code/', verify_email_code, name='verify-email-code'),
]

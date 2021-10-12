from django.contrib import admin
from django.urls import path, include
from .views import add_subscription

urlpatterns = [
    path('add-subscription/', add_subscription, name='add_subscription')
]

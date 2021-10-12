from django.contrib import admin
from django.urls import path, include
from .views import get_offers, get_company_offers_details

urlpatterns = [
    path('get-offers/', get_offers, name='get_offers'),
    path('get-detail-offers/<int:companyId>/', get_company_offers_details,
         name='get_company_offers_offers'),
]

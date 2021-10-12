from django.contrib import admin
from django.urls import path, include
from .views import get_company_opinions, add_company_opinion

urlpatterns = [
    path('get-company-opinions/<int:companyId>/', get_company_opinions,
         name='get_company_opinions'),
    path('add-company-opinion/', add_company_opinion, name='add_company_opinion')
]

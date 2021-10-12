from django.contrib import admin
from django.urls import path, include
from .views import get_detail_company
urlpatterns = [
    path('get-detail-company/<int:companyId>/',
         get_detail_company, name='get_detail_company')
]

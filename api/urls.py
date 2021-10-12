from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('company/', include('api.company.urls')),
    path('joboffer/', include('api.joboffer.urls')),
    path('user/', include('api.user.urls')),
    path('opinion/', include('api.opinion.urls')),
    path('subscription/', include('api.subscription.urls')),
]

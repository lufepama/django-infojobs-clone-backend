from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import JobOffer
from api.company.models import Company
from .serializers import JobOfferSerializer
# Create your views here.


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_offers(request, *args, **kwargs):
    offers = JobOffer.objects.all()
    products_serializer = JobOfferSerializer(offers, many=True)
    return JsonResponse({'success': 'There you have', 'data': products_serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_company_offers_details(request, companyId, *args, **kwargs):
    try:
        company = Company.objects.get(pk=companyId)
        offers_company = JobOffer.objects.filter(company=company)
        offers_company_serializer = JobOfferSerializer(
            offers_company, many=True)
        return JsonResponse({'success': 'There you have', 'data': offers_company_serializer.data}, status=status.HTTP_200_OK)

    except Company.DoesNotExist:
        return JsonResponse({'error': 'Ha habido un error'})

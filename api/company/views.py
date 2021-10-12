from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import Company
from .serializers import CompanySerializer
# Create your views here.


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_detail_company(request, companyId, *args, **kwargs):
    try:
        company = Company.objects.get(pk=companyId)
        company_serializer = CompanySerializer(company)

        return JsonResponse({'success': 'There you have', 'data': company_serializer.data}, status=status.HTTP_200_OK)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Ha habido un problema'})

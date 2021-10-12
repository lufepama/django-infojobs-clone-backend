from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from api.company.models import Company
from .models import Opinion
from .serializers import OpinionSerializer, PostOpinionSerializer
# Create your views here.


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_company_opinions(request, companyId, *args, **kwargs):
    try:
        company = Company.objects.get(pk=companyId)
        opinions_company = Opinion.objects.filter(company=company)
        opinions_serializer = OpinionSerializer(opinions_company, many=True)
        return JsonResponse({'success': 'There you have', 'data': opinions_serializer.data}, status=status.HTTP_200_OK)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Ha habido un problema...'})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_company_opinion(request, *args, **kwargs):
    try:
        companyId = request.data['companyId']
        current_user = request.user
        company = Company.objects.get(pk=companyId)
        serializer_data = {
            "company": company.name,
            "username": current_user.username,
            "title": request.data['title'],
            "description": request.data['description'],
            "rating": int(request.data['rating']),
        }
        opinion_company_serializer = PostOpinionSerializer(
            data=serializer_data)
        if opinion_company_serializer.is_valid():
            opinion_company_serializer.save()
            return JsonResponse({'success': 'Se ha aniadido correctamente', }, status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Ha habido un error...', 'info': opinion_company_serializer.error_messages})
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Ha habido un problema...'})

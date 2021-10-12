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
from api.user.models import User
from api.subscription.models import Subscription
# Create your views here.


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_subscription(request, *args, **kwargs):
    try:
        user = request.user
        company = request.data['companyId']
        query_company = Company.objects.filter(pk=int(company))
        query_user = User.objects.filter(username=user.username)

        if query_company and query_user:
            query, created = Subscription.objects.get_or_create(
                company=query_company.first(),
                user=query_user.first()
            )
            return JsonResponse({'success': 'Se ha aniadido correctamente', 'data': query.user.username})
        return JsonResponse({'error': 'Ha habido un problema'})

    except:
        return JsonResponse({'error': 'Ha habido un problema...'})

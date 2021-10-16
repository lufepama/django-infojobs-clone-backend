from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
import random
from .models import EmailConfirmation
# Create your views here.

def generate_random_code():
    return str(random.randrange(1000, 10000,4))

def sendEmailConfirmation(first_name, last_name, email,  code):
    variables = {"first_name":first_name, "last_name":last_name, "email":email, "verification_code": code}
    template = get_template("emailconfirmation/emailCodeConfirmation.html")
    real_content = template.render(variables)
    email_ = EmailMultiAlternatives(
        "Un correo de prueba",
        code,
        "automaticemaildjango@mail.com",
        [email]
    )
    email_.attach_alternative(real_content, "text/html")
    email_.send()
    print(email_)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_email_code(request, *args, **kwargs):
    
    try:
        
        email = request.data['email']
        query_email = EmailConfirmation.objects.filter(email=email)

        if (not query_email):
            new_code = generate_random_code()
            query = EmailConfirmation(email=email,verification_code=new_code)
            query.save()
            sendEmailConfirmation('Felipe', 'Paz Martinez', email, query.verification_code)
            return JsonResponse({'success':'Se ha generado el codigo correctamente','code':query.verification_code }, status=status.HTTP_201_CREATED)

        verify_code = query_email.first().verification_code
        sendEmailConfirmation('Felipe', 'Paz Martinez', email, verify_code)
        return JsonResponse({'success':'Se ha generado el codigo correctamente', 'code':verify_code }, status=status.HTTP_201_CREATED)
         
    except:
        return JsonResponse({'error':'ha habido un error' }, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_email_code(request, email,*args, **kwargs):
    try:
        query = EmailConfirmation.objects.get(email=email)
        return JsonResponse({'success':'Ha sido un exito', 'data':query.verification_code}, status=status.HTTP_200_OK)
        
    except EmailConfirmation.DoesNotExist:
        return JsonResponse({'error':'Ha habido un problema...'})

@api_view(['POST'])
@permission_classes([AllowAny])
def verify_email_code(request, *args, **kwargs):
    try:    
        email = request.data['email']
        verification_code = request.data['verificationCode']
        query = EmailConfirmation.objects.filter(email=email, verification_code = verification_code)
        if query:
            return JsonResponse({'success': 'Cuenta creada satisfactoriamente'}, status=status.HTTP_200_OK)
        return JsonResponse({'error':'Ha habido un problema.'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return JsonResponse({'error':'Ha habido un problema.....'}, status=status.HTTP_400_BAD_REQUEST)
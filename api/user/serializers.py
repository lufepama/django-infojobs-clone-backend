from inspect import currentframe
from django.db.models import fields
from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=100)
    birth_day = serializers.DateField()
    is_man = serializers.BooleanField()
    lives_in_spain = serializers.BooleanField()
    code_post = serializers.CharField(max_length=100)
    province = serializers.CharField(max_length=100)
    town = serializers.CharField(max_length=100)
    is_employed = serializers.BooleanField()
    company = serializers.CharField(max_length=100)
    position = serializers.CharField(max_length=100)
    date_employed = serializers.DateField()
    has_been_employed = serializers.BooleanField(default=False)
    accept_notifications = serializers.BooleanField()
    accept_terms = serializers.BooleanField()
    has_studies = serializers.BooleanField()
    studies_qualification = serializers.CharField(max_length=100)
    studies_speciality = serializers.CharField(max_length=100)
    studies_center = serializers.CharField(max_length=100)

    def validate_username(self, value):
        try:
            user = User.objects.get(username=value)
            if not user:
                raise serializers.ValidationError(
                    {'error': 'Ha habido un problema'})
        except:
            return value

    def validate(self, value):
        current_password = self.context['password']
        print('value', value['email'])
        if current_password in value['username'] or current_password in value['email']:
            print('entree')
            raise serializers.ValidationError(
                {'error': 'La contraseña no debe contener el usuario ni email'})
        return value

    def create(self, validated_data):
        current_password = validated_data['password']
        user = User(**validated_data)
        user.set_password(current_password)
        user.save()
        return user

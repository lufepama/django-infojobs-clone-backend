from re import M
from rest_framework import serializers
from django.contrib.auth import get_user_model

from api.company.models import Company
from api.opinion.models import Opinion
from api.user.models import User


class OpinionSerializer(serializers.BaseSerializer):

    def to_representation(self, instance):
        return instance.get_opinion_info


class PostOpinionSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=200)
    company = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    rating = serializers.IntegerField()

    def validate_company(self, value):
        try:
            company = Company.objects.get(name=value)
            if not company:
                return serializers.ValidationError(
                    {'error': 'Ha habido un problema'})
            return value

        except:
            return value

    def validate_username(self, value):
        try:
            user = User.objects.get(username=value)
            if not user:
                return serializers.ValidationError(
                    {'error': 'Ha habido un problema'})
            return value
        except:
            return value

    def validate_title(self, value):
        if len(value) == 0:
            return serializers.ValidationError(
                {'error': 'El titulo no puede estar vacio'})
        return value

    def validate_description(self, value):
        if len(value) == 0:
            return serializers.ValidationError(
                {'error': 'La descripcion no puede estar vacia'})
        return value

    def validate_rating(self, value):
        if value <= 0 or value >= 5:
            return serializers.ValidationError(
                {'error': 'El rating debe estar entre 0-5'})
        return value

    def create(self, validated_data):
        # current_password = validated_data['password']
        # user = User(**validated_data)
        # user.set_password(current_password)
        # user.save()
        # return user

        print('username', validated_data['username'])
        user = User.objects.get(username=validated_data['username'])
        company = Company.objects.get(name=validated_data['company'])
        print(validated_data['title'])
        new_opinion = Opinion(
            user=user,
            company=company,
            rating=validated_data['rating'],
            title=validated_data['title'],
            description=validated_data['description'],
        )
        new_opinion.save()
        return new_opinion

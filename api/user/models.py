from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'username'

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    is_man = models.BooleanField(default=False)
    lives_in_spain = models.BooleanField(default=False)
    code_post = models.CharField(max_length=10, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    is_employed = models.BooleanField(default=False)
    company = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    date_employed = models.DateField(blank=True, null=True)
    has_been_employed = models.BooleanField(default=False)
    accept_notifications = models.BooleanField(default=False)
    accept_terms = models.BooleanField(default=False)
    has_studies = models.BooleanField(default=False)
    studies_qualification =  models.CharField(max_length=100, blank=True, null=True)
    studies_speciality = models.CharField(max_length=100, blank=True, null=True)
    studies_center = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
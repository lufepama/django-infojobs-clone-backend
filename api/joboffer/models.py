from django.db import models
from django.utils import tree
from api.company.models import Company
# Create your models here.


class JobOffer(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_now_add=True)
    minimum_education = models.CharField(max_length=100)
    experience_years = models.IntegerField(default=0)
    requirement = models.CharField(max_length=100)
    teleworking = models.BooleanField(default=False)
    lower_salary = models.IntegerField(default=0)
    upper_salary = models.IntegerField(default=20)

    class Journey(models.TextChoices):
        complete = 'jornada completa',
        half = 'media jornada'

    journey = models.CharField(
        max_length=50,
        choices=Journey.choices,
        default=Journey.complete
    )
    experience = models.IntegerField(default=0)

    @property
    def get_company_info(self):
        return {
            'name': self.company.name,
            'location': self.company.town,
            'id': self.company.pk
        }

    @property
    def get_company_imagen(self):
        return self.company.image.url

    def __str__(self):
        return self.title

from django.db import models
from api.company.models import Company
from api.user.models import User

# Create your models here.


class Opinion(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(default=0)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200)

    @property
    def get_opinion_info(self):
        return {
            'username': self.user.username,
            'rating': self.rating,
            'title': self.title,
            'description': self.description,
        }

    def __str__(self):
        return self.company.name

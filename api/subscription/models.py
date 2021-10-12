from django.db import models
from api.company.models import Company
from api.user.models import User

# Create your models here.


class Subscription(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

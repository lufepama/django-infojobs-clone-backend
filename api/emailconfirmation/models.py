from django.db import models

# Create your models here.

class EmailConfirmation(models.Model):
    email = models.EmailField()
    verification_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.email
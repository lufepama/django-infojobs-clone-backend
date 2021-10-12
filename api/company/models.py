from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    town = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    web_url = models.CharField(max_length=200, default='http://google.es')
    workers = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    @property
    def get_company_info(self):
        return {
            'name': self.name,
            'description': self.description,
            'town': self.town,
            'province': self.province,
            'web': self.web_url,
            'image': self.image.url,
            'rating': self.rating,
            'workers': self.workers
        }

    def __str__(self):
        return self.name

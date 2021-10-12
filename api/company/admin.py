from django.contrib import admin
from django.db.models.expressions import CombinedExpression

# Register your models here.
from .models import Company

admin.site.register(Company)

# Generated by Django 3.1.3 on 2021-10-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accept_terms',
            field=models.BooleanField(default=False),
        ),
    ]

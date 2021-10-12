# Generated by Django 3.1.7 on 2021-10-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20211009_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='journey',
        ),
        migrations.RemoveField(
            model_name='company',
            name='publish_date',
        ),
        migrations.AddField(
            model_name='company',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
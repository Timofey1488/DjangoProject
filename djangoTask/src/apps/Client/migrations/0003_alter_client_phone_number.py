# Generated by Django 4.2.7 on 2023-11-24 11:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(limit_value=10), django.core.validators.MaxLengthValidator(limit_value=15)]),
        ),
    ]

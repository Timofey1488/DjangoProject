# Generated by Django 4.2.7 on 2023-11-11 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0003_alter_car_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=255),
        ),
    ]

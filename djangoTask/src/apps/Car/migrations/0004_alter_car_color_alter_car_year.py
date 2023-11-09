# Generated by Django 4.2.7 on 2023-11-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0003_remove_car_price_carsupplier_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('White', 'White'), ('Black', 'Black'), ('Silver', 'Silver'), ('Gray', 'Gray')], default='White', max_length=8),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(default=2023),
        ),
    ]

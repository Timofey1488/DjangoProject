# Generated by Django 4.2.7 on 2023-11-11 07:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CarDealer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDealerPromotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, verbose_name='Promotion name')),
                ('description', models.TextField(blank=True, verbose_name='Promotion Description')),
                ('start_date', models.DateTimeField(verbose_name='Promotion start date')),
                ('end_date', models.DateTimeField(verbose_name='Promotion end date')),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Promotion percent')),
            ],
            options={
                'verbose_name': 'Car Dealer Promotion',
                'verbose_name_plural': 'Car Dealer Promotions',
            },
        ),
        migrations.CreateModel(
            name='SupplierPromotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, verbose_name='Promotion name')),
                ('description', models.TextField(blank=True, verbose_name='Promotion Description')),
                ('start_date', models.DateTimeField(verbose_name='Promotion start date')),
                ('end_date', models.DateTimeField(verbose_name='Promotion end date')),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Promotion percent')),
                ('car_dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDealer.cardealer')),
            ],
            options={
                'verbose_name': 'Supplier Promotion',
                'verbose_name_plural': 'Supplier Promotions',
            },
        ),
    ]

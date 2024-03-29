# Generated by Django 4.2.7 on 2023-11-13 08:55

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0002_initial'),
        ('CarDealer', '0003_initial'),
        ('Discount', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDealerDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('count_to_get_discount', models.IntegerField(default=0)),
                ('percent', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('date_start', models.DateField(default=datetime.date.today)),
                ('date_end', models.DateField(default=models.DateField(default=datetime.date.today))),
                ('car_dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDealer.cardealer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SupplierDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('count_to_get_discount', models.IntegerField(default=0)),
                ('percent', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('date_start', models.DateField(default=datetime.date.today)),
                ('date_end', models.DateField(default=models.DateField(default=datetime.date.today))),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supplier.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='supplierpromotion',
            name='car_dealer',
        ),
        migrations.RemoveField(
            model_name='supplierpromotion',
            name='supplier',
        ),
        migrations.DeleteModel(
            name='CarDealerPromotion',
        ),
        migrations.DeleteModel(
            name='SupplierPromotion',
        ),
    ]

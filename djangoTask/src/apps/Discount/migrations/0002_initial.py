# Generated by Django 4.2.7 on 2023-11-11 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Discount', '0001_initial'),
        ('Supplier', '0001_initial'),
        ('CarDealer', '0001_initial'),
        ('Car', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierpromotion',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supplier.supplier'),
        ),
        migrations.AddField(
            model_name='cardealerpromotion',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.car', verbose_name='Car'),
        ),
        migrations.AddField(
            model_name='cardealerpromotion',
            name='car_dealer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDealer.cardealer'),
        ),
    ]

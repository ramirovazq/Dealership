# Generated by Django 2.1.1 on 2019-01-23 22:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('VehicleInventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name': 'Vehicle', 'verbose_name_plural': 'Vehicles'},
        ),
        migrations.AddField(
            model_name='vehicle',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='lot_number',
            field=models.CharField(max_length=300, null=True, verbose_name='Lot #'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_make',
            field=models.CharField(max_length=300, null=True, verbose_name='Make'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_model',
            field=models.CharField(max_length=300, null=True, verbose_name='Model'),
        ),
    ]
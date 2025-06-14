# Generated by Django 5.2 on 2025-06-07 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0013_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='is_available',
        ),
        migrations.AddField(
            model_name='hotel',
            name='address_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='address_kk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='address_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='city_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='city_kk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='city_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='country_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='country_kk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='country_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description_kk',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='name_kk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='services_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='services_kk',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='services_ru',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotels.room'),
        ),
    ]

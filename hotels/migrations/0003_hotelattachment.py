# Generated by Django 5.2 on 2025-04-23 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_hotel_time_stamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('image', models.ImageField(upload_to='images')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
            ],
        ),
    ]

# Generated by Django 5.2 on 2025-04-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_alter_hotelattachment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='star',
            field=models.IntegerField(choices=[(1, 'Tourist 1 Star'), (2, 'Standart 2 Star'), (3, 'Comfort 3 Star'), (4, 'First Class 4 Star'), (5, 'Luxury 5 Star')], default=0, verbose_name='Category'),
        ),
    ]

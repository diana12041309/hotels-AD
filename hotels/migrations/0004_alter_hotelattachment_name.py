# Generated by Django 5.2 on 2025-04-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_hotelattachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelattachment',
            name='name',
            field=models.CharField(blank=True, null=True),
        ),
    ]

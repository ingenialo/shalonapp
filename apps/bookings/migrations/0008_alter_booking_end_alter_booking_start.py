# Generated by Django 4.0 on 2022-08-23 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_delete_mockbooking_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

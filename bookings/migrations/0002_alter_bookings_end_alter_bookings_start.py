# Generated by Django 4.0 on 2022-08-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='end',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='start',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.0 on 2022-08-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_payment_agenda_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='agenda_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
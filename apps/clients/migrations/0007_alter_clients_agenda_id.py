# Generated by Django 4.0 on 2022-08-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_clients_agenda_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='agenda_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
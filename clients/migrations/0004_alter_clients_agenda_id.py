# Generated by Django 4.0 on 2022-08-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_clients_agenda_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='agenda_id',
            field=models.IntegerField(blank=True),
        ),
    ]

# Generated by Django 4.0 on 2022-09-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0016_alter_clients_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='document_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

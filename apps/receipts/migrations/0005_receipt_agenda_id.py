# Generated by Django 4.0 on 2022-08-22 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0004_alter_receipt_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='agenda_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]

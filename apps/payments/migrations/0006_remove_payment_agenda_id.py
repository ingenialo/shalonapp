# Generated by Django 4.0 on 2022-08-18 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_alter_payment_agenda_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='agenda_id',
        ),
    ]
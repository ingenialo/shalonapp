# Generated by Django 4.0 on 2022-08-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_alter_payment_agenda_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='agenda_id',
            field=models.IntegerField(blank=True),
        ),
    ]
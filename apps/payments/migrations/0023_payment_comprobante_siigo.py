# Generated by Django 4.0 on 2022-10-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0022_payment_facturable_electronica_alter_payment_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='comprobante_siigo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

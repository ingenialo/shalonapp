# Generated by Django 4.0 on 2022-08-22 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='receipt_id',
        ),
        migrations.AddField(
            model_name='product',
            name='agenda_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]

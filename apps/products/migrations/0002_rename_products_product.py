# Generated by Django 4.0 on 2022-08-22 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',
            new_name='Product',
        ),
    ]
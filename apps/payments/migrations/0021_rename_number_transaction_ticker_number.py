# Generated by Django 4.0 on 2022-10-08 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0020_alter_payment_options_alter_payment_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='number',
            new_name='ticker_number',
        ),
    ]
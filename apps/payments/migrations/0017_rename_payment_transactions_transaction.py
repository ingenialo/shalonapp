# Generated by Django 4.0 on 2022-08-22 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0016_alter_payment_transactions_amount_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payment_Transactions',
            new_name='Transaction',
        ),
    ]

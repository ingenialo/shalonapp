# Generated by Django 4.0 on 2022-08-20 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0013_rename_employee_name_payment_employee_code_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
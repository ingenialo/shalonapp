# Generated by Django 4.0 on 2022-08-22 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0017_rename_payment_transactions_transaction'),
        ('bookings', '0004_mock_bookings_alter_booking_notes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mock_bookings',
            new_name='MockBooking',
        ),
        migrations.AlterField(
            model_name='booking',
            name='Payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.payment'),
        ),
    ]

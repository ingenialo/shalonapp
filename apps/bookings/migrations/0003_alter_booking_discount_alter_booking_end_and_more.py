# Generated by Django 4.0 on 2022-08-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_alter_booking_options_booking_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='notes',
            field=models.CharField(blank=True, help_text='Bienvenido(a) a Shalon Lash Brow , Por favor llegar 5 min antes.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='provider',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='receipt_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 4.0 on 2022-10-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0019_payment_errores_payment_facturado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'pago', 'verbose_name_plural': 'pagos'},
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(blank=True, null=True, verbose_name='cantidad'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='change_amount',
            field=models.IntegerField(blank=True, null=True, verbose_name='cantidad cambio'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='employee_code_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='codigo empleado'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='employee_code_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='empleado codigo_nombre'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='location_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ubicacion'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paid_amount',
            field=models.IntegerField(blank=True, null=True, verbose_name='cantidad pagada'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='fecha_pago'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

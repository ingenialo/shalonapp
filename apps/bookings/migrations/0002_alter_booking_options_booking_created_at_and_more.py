# Generated by Django 4.0 on 2022-08-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'get_latest_by': 'created_at', 'ordering': ['-created_at', '-updated_at']},
        ),
        migrations.AddField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', null=True, verbose_name='created at'),
        ),
        migrations.AddField(
            model_name='booking',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', null=True, verbose_name='updated at'),
        ),
    ]

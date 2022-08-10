# Generated by Django 4.0 on 2022-08-10 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('number', models.IntegerField(null=True)),
                ('receipt_type', models.TextField(max_length=200)),
            ],
        ),
    ]

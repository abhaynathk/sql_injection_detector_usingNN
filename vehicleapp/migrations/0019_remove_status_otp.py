# Generated by Django 3.1.7 on 2021-04-16 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0018_descriptions_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='otp',
        ),
    ]
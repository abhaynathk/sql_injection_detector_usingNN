# Generated by Django 3.1.7 on 2021-04-19 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0023_feedbacks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='otp',
        ),
    ]

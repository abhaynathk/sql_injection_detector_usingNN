# Generated by Django 3.1.7 on 2021-04-15 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0014_auto_20210415_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descriptions',
            name='username',
        ),
    ]

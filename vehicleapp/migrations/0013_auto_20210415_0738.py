# Generated by Django 3.1.7 on 2021-04-15 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0012_notifications_des_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='descriptions',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='descriptions',
            name='mobilenumber',
        ),
    ]

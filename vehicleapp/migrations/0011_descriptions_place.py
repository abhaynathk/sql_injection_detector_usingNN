# Generated by Django 3.1.7 on 2021-04-14 07:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0010_user_details_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='descriptions',
            name='place',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]

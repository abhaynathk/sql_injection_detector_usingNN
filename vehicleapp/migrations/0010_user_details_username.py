# Generated by Django 3.1.7 on 2021-04-02 02:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0009_mechanics_details_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]

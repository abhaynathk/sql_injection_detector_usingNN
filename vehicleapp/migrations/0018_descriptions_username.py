# Generated by Django 3.1.7 on 2021-04-16 05:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0017_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='descriptions',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
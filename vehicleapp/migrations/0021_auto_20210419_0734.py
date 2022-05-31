# Generated by Django 3.1.7 on 2021-04-19 06:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0020_auto_20210418_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='user_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='descriptions',
            name='username',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
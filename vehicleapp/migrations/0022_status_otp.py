# Generated by Django 3.1.7 on 2021-04-19 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0021_auto_20210419_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='otp',
            field=models.CharField(max_length=150, null=True),
        ),
    ]

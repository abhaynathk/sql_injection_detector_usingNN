# Generated by Django 3.1.7 on 2021-04-19 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0022_status_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=100)),
            ],
        ),
    ]

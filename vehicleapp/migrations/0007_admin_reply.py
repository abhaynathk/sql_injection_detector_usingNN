# Generated by Django 3.1.7 on 2021-04-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0006_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=150)),
            ],
        ),
    ]
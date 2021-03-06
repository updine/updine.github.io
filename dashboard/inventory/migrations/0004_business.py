# Generated by Django 3.0.2 on 2020-01-19 00:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20200110_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('website', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-31 00:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fringe_api', '0004_auto_20181031_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_no',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number entered is invalid', regex='ˆ\\+?\\d{1,3}?[- ]?[6789]\\d{9}$')]),
        ),
    ]

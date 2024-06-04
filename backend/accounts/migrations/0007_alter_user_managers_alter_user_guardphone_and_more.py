# Generated by Django 5.0.4 on 2024-06-04 09:58

import accounts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_is_staff'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='guardPhone',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number', regex='^01[0-9]{8,9}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='userBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userGender',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

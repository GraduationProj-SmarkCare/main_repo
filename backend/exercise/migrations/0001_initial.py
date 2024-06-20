# Generated by Django 5.0.4 on 2024-06-18 18:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0016_alter_userextra_height_alter_userextra_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('exerciseAlarmCnt', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3)),
                ('exerciseTime1', models.TimeField(blank=True, null=True)),
                ('exerciseTime2', models.TimeField(blank=True, null=True)),
                ('exerciseTime3', models.TimeField(blank=True, null=True)),
                ('exerciseTime4', models.TimeField(blank=True, null=True)),
                ('exerciseTime5', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]

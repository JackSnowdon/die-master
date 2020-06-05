# Generated by Django 3.0.6 on 2020-06-05 11:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_darkdieroll_fate_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='darkdieroll',
            name='threshold',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
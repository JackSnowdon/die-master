# Generated by Django 3.0.6 on 2020-06-02 16:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20200522_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='darkdieroll',
            name='fate_points',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]

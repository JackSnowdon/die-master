# Generated by Django 3.0.6 on 2020-05-22 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darkdieroll',
            name='roll_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.DarkHeresyGame'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0009_rename_endgame_time_puzzlestatus_puzzle_finished_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-24 23:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hunt', '0007_puzzle_alter_teamgame_id_alter_teamtask_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeamGame',
            new_name='PuzzleStatus',
        ),
        migrations.AlterModelOptions(
            name='puzzle',
            options={'verbose_name': 'Puzzle', 'verbose_name_plural': '(Add) Puzzles'},
        ),
        migrations.AlterModelOptions(
            name='puzzlestatus',
            options={'verbose_name': 'Puzzle Status', 'verbose_name_plural': 'Puzzle Statuses'},
        ),
        migrations.AlterModelOptions(
            name='teamtask',
            options={'verbose_name': 'Team Task', 'verbose_name_plural': '(Add) Team Tasks'},
        ),
        migrations.AlterModelOptions(
            name='teamtaskstatus',
            options={'verbose_name': 'Team Task Status', 'verbose_name_plural': 'Team Task Statuses'},
        ),
        migrations.AlterModelOptions(
            name='tries',
            options={'verbose_name': 'Try', 'verbose_name_plural': 'Tries'},
        ),
    ]

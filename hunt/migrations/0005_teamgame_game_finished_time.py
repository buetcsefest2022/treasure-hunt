# Generated by Django 2.1.2 on 2019-01-09 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0004_auto_20190109_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamgame',
            name='game_finished_time',
            field=models.DateTimeField(null=True),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-24 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0006_tries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.IntegerField(unique=True)),
                ('pdf', models.FileField(null=True, upload_to='puzzle')),
                ('answer', models.CharField(max_length=100)),
                ('location_clue', models.FileField(null=True, upload_to='location')),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('endgame_key', models.CharField(blank=True, max_length=6, null=True)),
                ('penalty_key', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='teamgame',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teamtask',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teamtaskstatus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tries',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teamgame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hunt.puzzle'),
        ),
        migrations.AlterField(
            model_name='teamtaskstatus',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hunt.puzzle'),
        ),
        migrations.AlterField(
            model_name='tries',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hunt.puzzle'),
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]

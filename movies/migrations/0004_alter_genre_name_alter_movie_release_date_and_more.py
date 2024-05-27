# Generated by Django 5.0.3 on 2024-05-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_release_date_alter_movie_running_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='running_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tmdb_id',
            field=models.IntegerField(blank=True, unique=True),
        ),
    ]
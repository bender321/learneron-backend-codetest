# Generated by Django 3.2.8 on 2022-01-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphql_api', '0002_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ManyToManyField(to='graphql_api.Movie'),
        ),
    ]
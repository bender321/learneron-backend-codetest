# Generated by Django 3.2.8 on 2022-01-16 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphql_api', '0004_auto_20220116_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='date_of_birth',
            field=models.DateField(max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(max_length=4),
        ),
    ]

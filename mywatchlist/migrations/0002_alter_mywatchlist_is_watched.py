# Generated by Django 4.1 on 2022-09-20 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='is_watched',
            field=models.BooleanField(),
        ),
    ]
# Generated by Django 4.1 on 2022-09-20 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0003_alter_mywatchlist_is_watched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='is_watched',
            field=models.CharField(max_length=3),
        ),
    ]

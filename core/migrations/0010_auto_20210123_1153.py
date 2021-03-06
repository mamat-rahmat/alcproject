# Generated by Django 3.1.2 on 2021-01-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_post_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='blank_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exam',
            name='correct_score',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='exam',
            name='score_in_percentage',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='wrong_score',
            field=models.IntegerField(default=0),
        ),
    ]

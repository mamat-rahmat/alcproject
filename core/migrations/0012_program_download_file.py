# Generated by Django 3.1.2 on 2021-02-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210123_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='download_file',
            field=models.BooleanField(default=False),
        ),
    ]

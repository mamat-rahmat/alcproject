# Generated by Django 3.1.2 on 2020-11-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='bidang',
            field=models.CharField(choices=[('matematika', 'Matematika SMA'), ('fisika', 'Fisika SMA'), ('kimia', 'Kimia SMA'), ('biologi', 'Biologi SMA'), ('komputer', 'Komputer SMA'), ('ekonomi', 'Ekonomi SMA'), ('astronomi', 'Astronomi SMA'), ('geografi', 'Geografi SMA'), ('kebumian', 'Kebumian SMA'), ('matematika-smp', 'Matematika SMP'), ('ipa-smp', 'IPA SMP'), ('ips-smp', 'IPS SMP')], default='matematika', max_length=20),
        ),
    ]

# Generated by Django 3.1.2 on 2021-01-23 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210123_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='bidang',
            field=models.CharField(choices=[('matematika', 'Matematika SMA'), ('fisika', 'Fisika SMA'), ('kimia', 'Kimia SMA'), ('biologi', 'Biologi SMA'), ('komputer', 'Komputer SMA'), ('ekonomi', 'Ekonomi SMA'), ('astronomi', 'Astronomi SMA'), ('geografi', 'Geografi SMA'), ('kebumian', 'Kebumian SMA'), ('matematika-smp', 'Matematika SMP'), ('ipa-smp', 'IPA SMP'), ('ips-smp', 'IPS SMP'), ('matematika-sd', 'Matematika SD'), ('ipa-sd', 'IPA SD')], default='matematika', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bidang',
            field=models.CharField(choices=[('matematika', 'Matematika SMA'), ('fisika', 'Fisika SMA'), ('kimia', 'Kimia SMA'), ('biologi', 'Biologi SMA'), ('komputer', 'Komputer SMA'), ('ekonomi', 'Ekonomi SMA'), ('astronomi', 'Astronomi SMA'), ('geografi', 'Geografi SMA'), ('kebumian', 'Kebumian SMA'), ('matematika-smp', 'Matematika SMP'), ('ipa-smp', 'IPA SMP'), ('ips-smp', 'IPS SMP'), ('matematika-sd', 'Matematika SD'), ('ipa-sd', 'IPA SD')], default='matematika', max_length=20),
        ),
    ]
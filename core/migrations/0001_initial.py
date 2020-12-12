# Generated by Django 3.1.2 on 2020-11-06 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problemset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemset_name', models.CharField(max_length=100)),
                ('problem_file', models.FileField(upload_to='')),
                ('solution_file', models.FileField(upload_to='')),
                ('no01', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no02', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no03', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no04', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no05', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no06', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no07', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no08', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no09', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no10', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no11', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no12', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no13', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no14', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no15', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no16', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no17', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no18', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no19', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no20', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no21', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no22', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no23', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no24', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no25', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no26', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no27', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no28', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no29', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no30', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no31', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no32', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no33', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no34', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no35', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no36', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no37', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no38', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no39', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no40', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no41', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no42', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no43', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no44', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no45', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no46', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no47', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no48', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no49', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no50', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('add_essay', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=100)),
                ('open_registration_time', models.DateTimeField(blank=True, null=True)),
                ('close_registration_time', models.DateTimeField(blank=True, null=True)),
                ('tutor_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.program')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.program')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('problemset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.problemset')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.program')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graded', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=0)),
                ('no01', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no02', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no03', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no04', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no05', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no06', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no07', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no08', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no09', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no10', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no11', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no12', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no13', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no14', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no15', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no16', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no17', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no18', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no19', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no20', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no21', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no22', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no23', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no24', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no25', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no26', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no27', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no28', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no29', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no30', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no31', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no32', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no33', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no34', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no35', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no36', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no37', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no38', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no39', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no40', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no41', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no42', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no43', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no44', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no45', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no46', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no47', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no48', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no49', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('no50', models.CharField(choices=[('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='-', max_length=1)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.exam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

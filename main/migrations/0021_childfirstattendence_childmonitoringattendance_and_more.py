# Generated by Django 5.0.4 on 2024-05-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_pregnancy_birth_place_pregnancy_birth_weight_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildFirstAttendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_weight_below_2500grams', models.BooleanField(blank=True, null=True)),
                ('fourth_child_or_more', models.BooleanField(blank=True, null=True)),
                ('twin', models.BooleanField(blank=True, null=True)),
                ('orphan', models.BooleanField(blank=True, null=True)),
                ('death_of_siblings_under_age_of_5', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChildMonitoringAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default='2024-01-01')),
                ('anemia', models.BooleanField(blank=True, null=True)),
                ('body_temperature', models.CharField(blank=True, max_length=200, null=True)),
                ('mothers_milk', models.BooleanField(blank=True, null=True)),
                ('milk_substitute', models.BooleanField(blank=True, null=True)),
                ('motor_skills_improvement', models.BooleanField(blank=True, null=True)),
                ('white_lining_of_the_mouth', models.BooleanField(blank=True, null=True)),
                ('eyes_weaken', models.BooleanField(blank=True, null=True)),
                ('navel', models.CharField(choices=[('healed', 'healed'), ('redish', 'redish'), ('gives off smell', 'gives off smell')], max_length=200)),
                ('rashes_with_pus', models.BooleanField(blank=True, null=True)),
                ('yellowish_skin', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChildVaccineInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bcg_tuberclosis_injection_right_shoulder', models.DateField(default='2024-01-01')),
                ('polio_mouth_droplets', models.DateField(default='2024-01-01')),
                ('DPT_HB1_injection_left_thigh', models.DateField(default='2024-01-01')),
                ('measles_injection_right_thigh', models.DateField(default='2024-01-01')),
                ('vitamin_A_mouth_droplets', models.DateField(default='2024-01-01')),
                ('rota', models.DateField(default='2024-01-01')),
                ('pmeumoccocal', models.DateField(default='2024-01-01')),
            ],
        ),
    ]

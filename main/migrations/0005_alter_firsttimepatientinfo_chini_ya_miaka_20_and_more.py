# Generated by Django 5.0.1 on 2024-04-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_doctor_status_pregnance_jina_la_mtoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firsttimepatientinfo',
            name='chini_ya_miaka_20',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='firsttimepatientinfo',
            name='kifua_kikuu',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='firsttimepatientinfo',
            name='kisukari',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='firsttimepatientinfo',
            name='kuharibika_kwa_mimba_2_au_zaidi',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='firsttimepatientinfo',
            name='miaka_10_au_zaid_tokea_mimba_ya_mwisho',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='firsttimepatientinfo',
            name='ugonjwa_wa_moyo',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

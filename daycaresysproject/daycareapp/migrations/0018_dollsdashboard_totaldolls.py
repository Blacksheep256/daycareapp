# Generated by Django 5.0.6 on 2024-05-09 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycareapp', '0017_rename_baby_id_schoolfees_baby'),
    ]

    operations = [
        migrations.AddField(
            model_name='dollsdashboard',
            name='totaldolls',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
    ]

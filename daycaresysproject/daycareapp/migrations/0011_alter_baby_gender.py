# Generated by Django 5.0.4 on 2024-04-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycareapp', '0010_baby_gender_babysitter_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=128, null=True),
        ),
    ]
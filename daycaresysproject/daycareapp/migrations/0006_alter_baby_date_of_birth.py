# Generated by Django 5.0.4 on 2024-04-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycareapp', '0005_alter_babysitter_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='date_of_birth',
            field=models.DateField(max_length=20),
        ),
    ]

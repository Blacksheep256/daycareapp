# Generated by Django 5.0.4 on 2024-04-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycareapp', '0008_babysitter_address_babysitter_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babysitter',
            name='address',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='district',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='email',
            field=models.CharField(max_length=20),
        ),
    ]

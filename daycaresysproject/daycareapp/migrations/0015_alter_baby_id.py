# Generated by Django 5.0.6 on 2024-05-08 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycareapp', '0014_schoolfees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

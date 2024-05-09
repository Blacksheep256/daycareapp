# Generated by Django 5.0.4 on 2024-05-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycareapp', '0011_alter_baby_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=10)),
                ('unit_price', models.FloatField(max_length=10)),
                ('qty', models.FloatField(max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

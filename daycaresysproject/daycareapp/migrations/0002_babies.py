# Generated by Django 5.0.4 on 2024-04-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycareapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='babies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('parent_name', models.CharField(max_length=20)),
                ('guardian_name', models.CharField(max_length=20)),
                ('parent_phonenummber', models.CharField(max_length=20)),
                ('guardian_phonenumber', models.CharField(max_length=20)),
            ],
        ),
    ]
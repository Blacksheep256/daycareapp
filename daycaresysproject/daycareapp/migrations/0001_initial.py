# Generated by Django 5.0.4 on 2024-04-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='babysitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('nin', models.CharField(max_length=20)),
                ('phonenumber', models.CharField(max_length=20)),
            ],
        ),
    ]
# Generated by Django 5.0.6 on 2024-05-09 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daycareapp", "0018_dollsdashboard_totaldolls"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schoolfees",
            name="type_of_payment",
            field=models.CharField(
                choices=[("day", "Day"), ("halfday", "Halfday")],
                max_length=128,
                null=True,
            ),
        ),
    ]

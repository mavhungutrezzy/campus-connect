# Generated by Django 4.2 on 2023-10-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("applications", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bursaryapplication",
            name="date_applied",
            field=models.DateTimeField(),
        ),
    ]

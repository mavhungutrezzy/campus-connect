# Generated by Django 4.2 on 2023-10-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "prospectuses",
            "0007_rename_application_close_applicationdetail_application_close_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="admission_point_score",
            field=models.IntegerField(default=24),
        ),
    ]

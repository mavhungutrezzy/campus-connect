# Generated by Django 4.2 on 2023-10-13 07:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("prospectuses", "0009_subject_admissionpointscore"),
        ("applications", "0006_alter_bursaryapplication_notes"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("application_status", models.CharField(max_length=60)),
                ("application_date", models.DateField(null=True)),
                ("notes", models.TextField(max_length=255)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="prospectuses.course",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

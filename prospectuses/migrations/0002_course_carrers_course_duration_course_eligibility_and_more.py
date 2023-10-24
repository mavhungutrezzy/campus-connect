# Generated by Django 4.2 on 2023-10-08 09:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("prospectuses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="carrers",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="course",
            name="duration",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="course",
            name="eligibility",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="course",
            name="nqf_level",
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name="course",
            name="nqf_level_name",
            field=models.CharField(default="Higher Certificate", max_length=15),
        ),
        migrations.AddField(
            model_name="university",
            name="city",
            field=models.CharField(default="Pretoria", max_length=60),
        ),
        migrations.AddField(
            model_name="university",
            name="description",
            field=models.TextField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="university",
            name="logo",
            field=models.URLField(default="http://example.com", max_length=255),
        ),
        migrations.AddField(
            model_name="university",
            name="province",
            field=models.CharField(default="Gauteng", max_length=30),
        ),
        migrations.AddField(
            model_name="university",
            name="website",
            field=models.URLField(default="http://example.com", max_length=255),
        ),
        migrations.CreateModel(
            name="UndergraduateDetail",
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
                (
                    "application_fee_amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                ("application_method", models.CharField(max_length=25)),
                ("application_url", models.URLField(default="http://example.com")),
                ("application_open", models.DateField()),
                ("application_close", models.DateField()),
                (
                    "university",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="prospectuses.university",
                    ),
                ),
            ],
        ),
    ]

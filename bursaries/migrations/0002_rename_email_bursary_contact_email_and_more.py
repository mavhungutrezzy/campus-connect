# Generated by Django 4.2 on 2023-10-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bursaries", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bursary",
            old_name="email",
            new_name="contact_email",
        ),
        migrations.RenameField(
            model_name="bursary",
            old_name="eligibility_description",
            new_name="eligibility_requirements",
        ),
        migrations.RenameField(
            model_name="bursary",
            old_name="organization_name",
            new_name="provider",
        ),
        migrations.RenameField(
            model_name="bursary",
            old_name="organization_description",
            new_name="provider_description",
        ),
        migrations.RemoveField(
            model_name="bursary",
            name="bursary_application_url",
        ),
        migrations.RemoveField(
            model_name="bursary",
            name="institution_supported",
        ),
        migrations.RemoveField(
            model_name="bursary",
            name="is_full_coverage",
        ),
        migrations.AddField(
            model_name="bursary",
            name="application_method",
            field=models.CharField(default="Online Application", max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="bursary",
            name="application_url",
            field=models.URLField(default="https://example.com/bursaries"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="bursary",
            name="bursary_name",
            field=models.CharField(default="TFG Scholarship", max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="bursary",
            name="covers_full_tuition",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="bursary",
            name="supported_institutions",
            field=models.JSONField(default="UJ"),
            preserve_default=False,
        ),
    ]

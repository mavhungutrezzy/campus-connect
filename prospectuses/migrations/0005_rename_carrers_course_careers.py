# Generated by Django 4.2 on 2023-10-08 09:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "prospectuses",
            "0004_alter_undergraduatedetail_application_fee_amount_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="carrers",
            new_name="careers",
        ),
    ]

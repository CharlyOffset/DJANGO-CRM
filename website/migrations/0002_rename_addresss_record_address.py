# Generated by Django 5.2.1 on 2025-05-09 14:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="record",
            old_name="addresss",
            new_name="address",
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-01-13 18:07
from django.db import migrations


def apply(apps, schema_editor):
    # sqlite does not allow ALTER COLUMN, but also isn't affected by this issue
    if "postgresql" in schema_editor.connection.vendor:
        schema_editor.execute("ALTER TABLE morango_transfersession ALTER COLUMN transfer_stage DROP NOT NULL")
        schema_editor.execute("ALTER TABLE morango_transfersession ALTER COLUMN transfer_stage_status DROP NOT NULL")


def revert(apps, schema_editor):
    # sqlite does not allow ALTER COLUMN, but also isn't affected by this issue
    if "postgresql" in schema_editor.connection.vendor:
        schema_editor.execute("ALTER TABLE morango_transfersession ALTER COLUMN transfer_stage SET NOT NULL")
        schema_editor.execute("ALTER TABLE morango_transfersession ALTER COLUMN transfer_stage_status SET NOT NULL")


class Migration(migrations.Migration):
    """
    Applies nullable change made to 0018_auto_20210714_2216.py after it was released
    """

    dependencies = [
        ("morango", "0019_auto_20220113_1807"),
    ]

    operations = [
        migrations.RunPython(apply, reverse_code=revert),
    ]

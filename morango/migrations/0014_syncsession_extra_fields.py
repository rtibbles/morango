# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2019-12-30 18:28
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("morango", "0013_auto_20190627_1513"),
    ]

    operations = [
        migrations.AddField(
            model_name="syncsession",
            name="extra_fields",
            field=models.TextField(default="{}"),
        ),
    ]

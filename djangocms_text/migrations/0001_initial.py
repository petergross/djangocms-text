# Generated by Django 5.0.1 on 2024-01-12 23:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
    ]

    operations = [
        migrations.CreateModel(
            name="Text",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="%(app_label)s_%(class)s",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                ("body", models.TextField(verbose_name="body")),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-17 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0016_libraryreferences"),
    ]

    operations = [
        migrations.CreateModel(
            name="IntroEvolution",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="IntroMission",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
    ]

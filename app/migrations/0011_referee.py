# Generated by Django 4.2.3 on 2023-07-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_coach"),
    ]

    operations = [
        migrations.CreateModel(
            name="Referee",
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
                ("fullname", models.CharField(max_length=200)),
                ("object", models.CharField(max_length=200, null=True)),
                ("sex", models.CharField(max_length=5)),
                ("social_network", models.CharField(max_length=200, null=True)),
                ("date_of_birth", models.DateField()),
                ("home_live", models.CharField(max_length=200, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                ("career", models.CharField(max_length=200, null=True)),
                ("archie", models.TextField()),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-08 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_remove_blog_category_alter_blog_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="photo",
            name="category",
        ),
        migrations.AddField(
            model_name="photo",
            name="category",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
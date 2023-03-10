# Generated by Django 4.1.5 on 2023-01-23 19:25

from ..services import image_paths_builders
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chat",
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
                ("title", models.CharField(max_length=50)),
                ("invite_link", models.CharField(max_length=255)),
                ("greeting_text", models.TextField()),
                (
                    "greeting_image",
                    models.ImageField(upload_to=image_paths_builders.greeting_image_path),
                ),
            ],
        ),
    ]

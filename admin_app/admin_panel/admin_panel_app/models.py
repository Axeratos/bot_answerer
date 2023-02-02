from django.db import models
from .services import greeting_image_path, image_size_validator


class Chat(models.Model):
    title = models.CharField(max_length=50)
    invite_link = models.CharField(max_length=255)
    greeting_text = models.TextField(max_length=1024)
    greeting_image = models.ImageField(upload_to=greeting_image_path, validators=[image_size_validator])

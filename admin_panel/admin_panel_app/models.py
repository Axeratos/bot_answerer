from django.db import models
from .services import greeting_image_path


class Chat(models.Model):
    title = models.CharField(max_length=50)
    invite_link = models.CharField(max_length=255)
    greeting_text = models.TextField()
    greeting_image = models.ImageField(upload_to=greeting_image_path)

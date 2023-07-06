from django.db import models
from django.contrib.auth.models import User

from homepage.managers import PostManager


class Post(models.Model):
    objects = PostManager()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    content = models.TextField(max_length=512)
    image = models.ImageField()

    def __str__(self) -> str:
        return f'"{self.title}" by {self.author}'

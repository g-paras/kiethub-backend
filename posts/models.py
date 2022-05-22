from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="posts", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255, null=True)
    body = models.TextField()

    def __str__(self) -> str:
        return f"{self.title} | {self.author}"
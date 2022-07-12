from django.db import models
from profiles.models import Profile

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="posts", blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} | {self.author}"

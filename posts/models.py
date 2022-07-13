from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from profiles.models import Profile

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="posts", blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    tags = models.CharField(max_length=255, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + '-' + get_random_string(length=6)

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title} | {self.author}"

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AuthModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="auth_status"
    )
    is_verified = models.BooleanField("is_verified", default=False)
    auth_token = models.UUIDField("auth_token", null=True)
    # created_at = models.DateTimeField("created_at", auto_now=True)

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class AuthModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="auth_status"
    )
    is_verified = models.BooleanField("is_verified", default=False)
    auth_token = models.UUIDField("auth_token", null=True)
    # created_at = models.DateTimeField("created_at", auto_now=True)


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), blank=False, unique=True)
    is_verified = models.BooleanField(
        _("verified"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as verified. "
        ),
    )
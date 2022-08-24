from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from uuid import uuid4

from .utils import send_verification_email
from .models import AuthModel


@receiver(post_save, sender=User)
def send_email_verification(sender, instance, created, **kwargs):
    if created:
        auth_model = AuthModel.objects.create(user=instance)
        auth_model.auth_token = uuid4()
        auth_model.save()

        send_verification_email(instance)

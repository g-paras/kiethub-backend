from django.db import models
from django.contrib.auth.models import User
from .choices import Course, Specialization
import random


def random_about():
    return random.choice(
        (
            [
                "I love to code",
                "Hey there, I am on KietHub",
                "Talk is Cheap, show me the code",
            ]
        )
    )


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    dob = models.DateField(null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    course = models.CharField(max_length=5, choices=Course.choices, null=True)
    specialization = models.CharField(
        max_length=5, choices=Specialization.choices, null=True
    )
    enrolled_year = models.DateField(null=True)
    graduation_year = models.DateField(null=True)
    contact = models.CharField(max_length=10, null=True)
    github = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    profile_image = models.ImageField(
        upload_to="profile",
        default="profile/default-avatar_r01tfd.jpg",
        null=True,
        blank=True,
    )
    about_me = models.CharField(max_length=200, default=random_about)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    # following_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} | {self.course} | {self.specialization}"

    # def get_following_count(self):
    #     return len(self.following)

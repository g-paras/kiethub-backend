from django.db import models
from django.contrib.auth.models import User

course_choices = ["B.Tech", "MCA", "M.Tech", "MBA"]
course_choices = [(str(i), j) for i, j in enumerate(course_choices)]

# Create your models here.
class Profile(models.Model):
    # name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    course = models.CharField(max_length=10, choices=course_choices, default="B.Tech")
    specialization = models.CharField(max_length=50, null=True)
    enrolled_year = models.DateField(null=True)
    current_year = models.IntegerField(null=True)
    contact = models.IntegerField(null=True)
    github = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    # library_id = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"Profile<user={self.user}, ...>"

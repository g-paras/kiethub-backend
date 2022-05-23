from django.db import models
from django.contrib.auth.models import User

course_choices = ["B.Tech", "MCA", "M.Tech", "MBA"]
course_list = [(str(i), j) for i, j in enumerate(course_choices)]

branch_choice = ["ECE", "EEE", "IT", "CO", "CSE", "CSIT", "ME", "CE"]
branch_list = [(str(i), j) for i, j in enumerate(branch_choice)]

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField(null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    course = models.CharField(max_length=10, choices=course_list, default=0)
    specialization = models.CharField(max_length=50, null=True)
    enrolled_year = models.DateField(null=True)
    graduation_year = models.DateField(null=True)
    contact = models.CharField(max_length=10, null=True)
    github = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    profile_image = models.ImageField(upload_to="profile", null=True, blank=True)

    def __str__(self):
        return f"{self.user} | {course_choices[int(self.course)]} | {self.specialization}"

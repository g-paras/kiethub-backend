from django.db import models
from django.contrib.auth.models import User

course_choices = ['B.Tech', 'MCA', 'M.Tech', 'MBA']
course_list = [(str(i), j) for i, j in enumerate(course_choices)]

branch_choice = ['ECE', 'EEE', 'IT', 'CO', 'CSE', 'CSIT', 'ME', 'CE']
branch_list = [(str(i), j) for i, j in enumerate(branch_choice)]

# Create your models here.
class Profile(models.Model):
    # name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    course = models.CharField(max_length=10, choices=course_list, default='B.Tech')
    specialization = models.CharField(max_length=50, null=True)
    enrolled_year = models.DateField(null=True)
    current_year = models.IntegerField(null=True)
    contact = models.CharField(max_length=10, null=True)
    section = models.CharField(max_length=1, null=True)
    github = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    profile = models.ImageField(upload_to="profile", null=True, blank=True)
    # library_id = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.user}, {course_choices[int(self.course)]}, {self.specialization}, {self.current_year}"
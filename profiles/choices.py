from django.db import models

class Course(models.TextChoices):
    BTECH = 'BTech', 'Bachelor of Technology'
    MCA = 'MCA', 'Masters of Computer Application'


class Specialization(models.TextChoices):
    ECE = 'ECE', 'Electronics & Communication'
    IT = 'IT', 'Information & Technology'
    EEE = 'EEE', 'Electrical and Electronics Engineering'
    CSE = 'CSE', 'Computer Science Engineeering'
    ME = 'ME', 'Mechanical Engineering'
    CE = 'CE', 'Civil Engineering'
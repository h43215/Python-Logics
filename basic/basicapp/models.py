from django.db import models


# Create your models here.
class StudentInfo(models.Model):
    fname =models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    DOB = models.DateField()

class TeacherInfo(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)


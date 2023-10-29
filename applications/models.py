from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BursaryApplication(models.Model):
    __tablename__ = "bursary_applications"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bursary = models.CharField(max_length=100)
    application_status = models.CharField(max_length=60)
    application_date = models.DateField(null=True)
    notes = models.TextField(max_length=255)


class CourseApplication(models.Model):
    __tablename__ = "course_applications"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    application_status = models.CharField(max_length=60)
    application_date = models.DateField(null=True)
    notes = models.TextField(max_length=255)

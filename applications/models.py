from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BursaryApplication(models.Model):
    """
    Model representing a Bursary Application.

    This model stores information about a bursary application, including the user who applied, the bursary being applied for, any notes associated with the application, and the date the application was submitted.

    Attributes:
        user (ForeignKey): The user who submitted the application.
        bursary (ForeignKey): The bursary being applied for.
        notes (TimeField): Any notes associated with the application.
        date_applied (DateTimeField): The date and time the application was submitted.

    Example:
        ```python
        application = BursaryApplication(user=user, bursary=bursary, notes=notes)
        application.save()
        ```"""

    __tablename__ = "bursary_applications"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bursary = models.CharField(max_length=100)
    application_status = models.CharField(max_length=60)
    application_date = models.DateField(null=True)
    notes = models.TextField(max_length=255)


class CourseApplication(models.Model):
    """
    Model representing a Bursary Application.

    This model stores information about a bursary application, including the user who applied, the bursary being applied for, any notes associated with the application, and the date the application was submitted.

    Attributes:
        user (ForeignKey): The user who submitted the application.
        bursary (ForeignKey): The bursary being applied for.
        notes (TimeField): Any notes associated with the application.
        date_applied (DateTimeField): The date and time the application was submitted.

    Example:
        ```python
        application = BursaryApplication(user=user, bursary=bursary, notes=notes)
        application.save()
        ```"""

    __tablename__ = "course_applications"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    application_status = models.CharField(max_length=60)
    application_date = models.DateField(null=True)
    notes = models.TextField(max_length=255)

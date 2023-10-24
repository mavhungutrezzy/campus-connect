from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

User = get_user_model()


class University(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=25)
    website = models.URLField(max_length=255)
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    logo_url = models.URLField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ApplicationInformation(models.Model):
    application_fee_amount = models.DecimalField(decimal_places=2, max_digits=5)
    application_methods = (
        ("Online", "Apply Online"),
        ("In-Person", "Apply In-Person"),
    )
    application_method = models.CharField(
        max_length=20, choices=application_methods, default="Online"
    )

    application_url = models.URLField()
    application_open_date = models.DateField()
    application_close_date = models.DateField()
    additional_information = RichTextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Course(models.Model):
    name = models.CharField(max_length=255)
    nqf_level = models.IntegerField(default=5)
    nqf_level_name = models.CharField(max_length=15)
    duration_in_years = models.IntegerField(default=1)
    eligibility = RichTextField(null=True, blank=True)
    careers = models.JSONField(null=True, blank=True)
    admission_point_score = models.IntegerField(default=24)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

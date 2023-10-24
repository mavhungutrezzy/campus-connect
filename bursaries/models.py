from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify


class Bursary(models.Model):
    __tablename__ = "bursaries"
    bursary_name = models.CharField(max_length=122)
    slug = models.SlugField(unique=True, blank=True)
    provider = models.CharField(max_length=60)
    provider_description = RichTextField()
    bursary_description = RichTextField()
    eligibility_requirements = RichTextField()
    application_deadline = models.DateField()
    application_method = models.CharField(max_length=122)
    application_url = models.URLField()
    bursary_coverage = models.JSONField()
    field_of_study = models.JSONField()
    contact_email = models.EmailField()
    contact_number = models.CharField(max_length=13)
    covers_full_tuition = models.BooleanField(default=True)
    supported_institutions = models.JSONField()

    def __str__(self):
        return self.bursary_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.bursary_name)
        super(Bursary, self).save(*args, **kwargs)

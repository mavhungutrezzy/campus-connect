from django.db import models
from django.contrib.auth import get_user_model

from bursaries.models import Bursary

User = get_user_model()


class BursaryFavorite(models.Model):
    """
    Represents a favorite relationship between a user and a bursary.

    Attributes:
        user (ForeignKey): The user who favorited the bursary.
        bursary (ForeignKey): The bursary that was favorited.
        date_favorited (DateField): The date when the bursary was favorited."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bursary = models.ForeignKey(Bursary, on_delete=models.CASCADE)
    date_favorited = models.DateField(auto_now_add=True)

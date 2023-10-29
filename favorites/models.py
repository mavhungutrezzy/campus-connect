from django.contrib.auth import get_user_model
from django.db import models

from bursaries.models import Bursary

User = get_user_model()


class BursaryFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bursary = models.ForeignKey(Bursary, on_delete=models.CASCADE)
    date_favorited = models.DateField(auto_now_add=True)

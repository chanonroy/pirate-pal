from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Links UserProfile to User model instance
    user = models.OneToOneField(User)

    # Additional attributes
    website = models.CharField(max_length=50, blank=True, null=True)

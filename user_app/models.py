from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class RedditUser(AbstractUser):
    homepage = models.URLField(null=True, blank=True)
    display_name = models.CharField(max_length=40, null=True, blank=True)
    age = models.IntegerField(default=0)
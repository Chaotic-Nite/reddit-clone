from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class RedditUser(AbstractUser):
    '''
        Custom User Model to fit all Reddit Needs
    '''
    sub_reddits = models.ManyToManyField('self',symmetrical=False, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
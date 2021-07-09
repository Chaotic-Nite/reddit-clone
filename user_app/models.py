from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from subreddit.models import SubReddit

# Create your models here.
class RedditUser(AbstractUser):
    # Change over to SubReddit when other apps are merged
    karma = models.IntegerField(default=0)
    sub_reddits = models.ManyToManyField(SubReddit, symmetrical=False, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


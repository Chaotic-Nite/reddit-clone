from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField()
  upvote = models.IntegerField()
  downvote = models.IntegerField()
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title


  def votes(self):
    return self.upvote-self.downvote
from django.db import models
from user_app.models import RedditUser
from subreddit.models import SubReddit
from django.utils import timezone


class CommonFieldsMixin(models.Model):
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    author = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)

    def votes(self):
        return self.upvote - self.downvote

    class Meta:
        abstract = True

class Post(CommonFieldsMixin, models.Model):
    ''' 
        Special information for the Posts
    '''
    TYPE_POST = (('Text', 'Text'), ('Link', 'Link'), ('Image', 'Image'))

    type_post = models.CharField(max_length=7, choices=TYPE_POST, default='Text')
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    url_post = models.URLField(blank=True, null=True)
    subreddit = models.ForeignKey(SubReddit, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


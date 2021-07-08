from user_app.models import RedditUser
from django.db import models
from user_app.models import RedditUser
from post_app.models import Post

class Subreddit(models.Model):
    '''
        Subreddits and their information.
    '''
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    # In creation we add who ever created it to this
    moderators = models.ManyToManyField(RedditUser, symmetrical=False, blank=True)
    posts = models.ManyToManyField(Post, symmetrical=False, blank=True)


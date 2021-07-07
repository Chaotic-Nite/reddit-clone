# from user_app.models import RedditUser
# from django.db import models
# from user_app.models import RedditUser
# from post_app.models import Post


# class Moderator(models.Model):
#     is_moderator = models.BooleanField(default=False)
#     user = models.ForeignKey(RedditUser, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username

# class Subreddit(models.Model):
#     '''
#         Subreddits and their information.
#     '''
#     title = models.CharField(max_length=150)
#     description = models.CharField(max_length=150)
#     # In creation we add who ever created it to this
#     moderators = models.ManyToManyField(RedditUser, symmetrical=False, blank=True)
#     posts = models.ManyToManyField(Post, symmetrical=False, blank=True)

#     def __str__(self):
#         return self.name

from django.db import models
# from authentication.models import RedditUser
from post_app.models import Post


class Moderator(models.Model):
    is_moderator = models.BooleanField(default=False)
    # user = models.ForeignKey(RedditUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class SubReddit(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=200)
    # subscriber = models.ManyToManyField(RedditUser, related_name='user')
    moderator = models.ManyToManyField(Moderator, related_name='moderator')

    def __str__(self):
        return self.name
from django.db import models
from user_app.models import RedditUser
from django.utils import timezone


# Constructed Mixin for both Post and Comment
class Post(models.Model):
    title = models.CharField(max_length=150)
    url_post = models.URLField()
    # comments = models.ManyToManyField(Comment, symmetrical=False, blank=True)
    content = models.TextField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    created_by = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)

    def votes(self):
        return self.upvote - self.downvote

    def __str__(self):
        return self.title

    # class Meta:
    #     abstract = True


# class Comment(CommonFieldsMixin, models.Model):
#     ''' 
#         The common mixin contants all we'd need for comments so it just passes
#     '''
#     pass

# class Post(CommonFieldsMixin, models.Model):
#     ''' 
#         Special information for the Posts
#     '''
#     title = models.CharField(max_length=150)
#     url_post = models.URLField()
#     comments = models.ManyToManyField(Comment, symmetrical=False, blank=True)

#     def __str__(self):
#         return self.title

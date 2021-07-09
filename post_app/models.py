from django.db import models
from user_app.models import RedditUser
from django.utils import timezone


class CommonFieldsMixin(models.Model):
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_by = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def like_dislike(self):
        return self.like - self.dislike

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
    #comments = models.ManyToManyField(Comment, symmetrical=False, blank=True)
from django.db import models

class Moderator(models.Model):
    is_moderator = models.BooleanField(default=False)
    user = models.ForeignKey('user_app.RedditUser', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


class SubReddit(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=200)
    moderator = models.ManyToManyField(Moderator, related_name='moderator')

    def __str__(self):
        return self.name
    
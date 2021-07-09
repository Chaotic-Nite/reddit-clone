from django.contrib import admin
from subreddit.models import SubReddit, Moderator

admin.site.register(SubReddit)
admin.site.register(Moderator)

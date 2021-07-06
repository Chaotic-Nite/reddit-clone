from django.contrib import admin

from user_app.models import RedditUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(RedditUser, UserAdmin)
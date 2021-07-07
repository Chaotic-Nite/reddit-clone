from user_app.models import RedditUser
from django import forms

from post_app.models import Post


class AddPostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'url_post']


  title = forms.CharField(max_length=150)
  url_post = forms.URLField()
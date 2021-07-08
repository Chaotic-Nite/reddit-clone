# from user_app.models import RedditUser
from django import forms

from post_app.models import Post, Images


class AddPostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'url_post', 'content']



class ImgForm(forms.ModelForm):
  class Meta:
    model = Images
    fields = ['name', 'hotel_Main_img']


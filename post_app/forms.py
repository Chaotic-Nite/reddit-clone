# from user_app.models import RedditUser
from django import forms

from post_app.models import Post
class AddPostForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)

        self.fields['type_post'].inital = dict(Post.TYPE_POST).get('Text')
  
  class Meta:
    model = Post
    fields = ['title', 'type_post', 'url_post', 'content', 'image']

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


class PostEditForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(PostEditForm, self).__init__(*args, **kwargs)

        self.fields['type_post'].inital = dict(Post.TYPE_POST).get('Text')
  
  class Meta:
    model = Post
    fields = ['title', 'type_post', 'url_post', 'content', 'image']


class PostDeleteForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(PostDeleteForm, self).__init__(*args, **kwargs)

        self.fields['type_post'].inital = dict(Post.TYPE_POST).get('Text')
        self.fields['content'].inital = '[delete]'
        self.fields['image'].inital = ''
        self.fields['url_post'].inital = ''
  
  class Meta:
    model = Post
<<<<<<< HEAD
    fields = ['type_post', 'url_post', 'content', 'image']
=======
    fields = ['title', 'url_post', 'comments']
>>>>>>> 7a283c0... Having trouble creating an editing posts

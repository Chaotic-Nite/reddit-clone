from django import forms

from post_app.models import Post

class AddPostForm(forms.Form):
  title = forms.CharField(max_length=50)
  content = forms.CharField(widget=forms.Textarea)
  upvote = forms.IntegerField()
  downvote = forms.IntegerField()
  created_at = forms.DateTimeField()

from user_app.models import RedditUser
from django import forms

from post_app.models import CommonFieldsMixin, Post

# class AddCommonFieldsMixinForm(forms.Form):
#   content = forms.CharField(widget=forms.Textarea)
#   likes = forms.IntegerField()
#   dislikes = forms.IntegerField()
#   created_by = forms.ModelChoiceField(queryset=RedditUser.objects.all())
#   created_at = forms.DateTimeField()

class AddPostForm(forms.ModelForm):
  class Meta:
    model = Post

from django import forms
from comments.models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body',
        ]
        widgets = {'body': forms.Textarea(attrs={'rows':4, 'cols':80})}


class PostEditForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['body']



class DeleteCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeleteCommentForm, self).__init__(*args, **kwargs)

        self.fields['body'].inital = '[deleted]'
        
    class Meta:
        model = Comment
        fields = ['body']
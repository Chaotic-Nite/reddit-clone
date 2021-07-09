from django import forms
from user_app.models import RedditUser

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = RedditUser
        fields = ['username', 'password']
        # change fields to sub_reddits?

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
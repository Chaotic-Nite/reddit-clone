from django import forms
from user_app.models import RedditUser

class SignupForm(forms.ModelForm):
    class Meta:
        model = RedditUser
        fields = ['username', 'password']
        # change fields to sub_reddits?

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)





# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = RedditUser
#         fields = ['username', 'password', 'email','display_name', 'age']
#         # should I change fields to sub_reddits

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=20)
#     password = forms.CharField(max_length=20)

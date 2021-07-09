from django.shortcuts import render
from user_app.forms import LoginForm, SignupForm
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from user_app.models import RedditUser
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup_view(request):
    ''' View to Signup to the Application's TwitterUser Model '''
    if request.method ==  'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['password'] == data['confirm_password']:
                RedditUser.objects.create_user(username=data['username'], password=data['password'])
                login_user = authenticate(request, username=data['username'], password=data['password'])
                if login_user:
                    login(request, login_user)
                    return HttpResponseRedirect(reverse('homepage'))
    
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    ''' View to Login to Application '''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
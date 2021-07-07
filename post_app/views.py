from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect, reverse
from post_app.models import CommonFieldsMixin, Post
from post_app.forms import AddPostForm

# Create your views here.

def index(request):
  posts = Post.objects.all()
  return render(request, 'index.html', {'posts': posts})

def post_detail(request, post_id: int):
  post = Post.objects.get(id=post_id)
  return render(request, 'post_detail', {'post': post})

def add_post(request):
  if request.method == 'POST':
    form = AddPostForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('homepage'))
    form = AddPostForm()
    return render(request, 'generic_form.html', {'form': form})
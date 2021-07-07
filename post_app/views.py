from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect, reverse
from post_app.models import CommonFieldsMixin, Post
from post_app.forms import AddPostForm
from django.views.generic.edit import CreateView


# Create your views here.

def index(request):
  posts = Post.objects.all()
  return render(request, 'index.html', {'posts': posts})

def post_detail(request, post_id: int):
  post = Post.objects.get(id=post_id)
  return render(request, 'post_detail.html', {'post': post})

def add_post(request):
  if request.method == 'POST':
    form = AddPostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.created_by = request.user
      post.save()
    return HttpResponseRedirect(reverse('homepage'))
  form = AddPostForm()
  return render(request, 'generic_form.html', {'form': form})




def edit_post(request, post_id: int):
  posts = Post.objects.get(id=post_id)
  if request.method == 'POST':
    form = AddPostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.created_by = request.user
      post.save()
    return HttpResponseRedirect(reverse('post_detail', args=(post_id,)))
  
  form = AddPostForm(initial={
    'title': posts.title,
    'url_post': posts.url_post,
    # 'comments': posts.comments
    })
  return render(request, 'generic_form.html', {'form': form})
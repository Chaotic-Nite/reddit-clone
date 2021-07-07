<<<<<<< HEAD
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect, reverse
from post_app.models import Post
from post_app.forms import AddPostForm

# Create your views here.

def post_detail(request, post_id: int):
  post = Post.objects.get(id=post_id)
  return render(request, 'post_detail', {'post': post})


def add_post(request):
  if request.method == 'POST':
    form = AddPostForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      new_post = Post.objects.create(
        content=data['content'],
        likes=data['likes'],
        dislikes=data['dislikes'],
        created_by=data['created_by'],
        created_at=data['created_at']
      )
      return HttpResponseRedirect(reverse('homepage'))
    form = AddPostForm()
    return render(request, 'generic_form.html', {'form': form})
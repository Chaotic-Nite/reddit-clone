from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponseRedirect, reverse
from post_app.models import Post
from post_app.forms import AddPostForm


# Create your views here.

def index(request):
  if Post.objects.filter(pk=0).exists():
    posts = Post.objects.all()
  else:
    posts = False
  return render(request, 'index.html', {'posts': posts})


def upvote_view(request, post_id: int):
  post = Post.objects.get(id=post_id)
  post.upvote += 1
  post.save()
  return HttpResponseRedirect(reverse('homepage'))

def downvote_view(request, post_id: int):
  post = Post.objects.get(id=post_id)
  post.downvote += 1
  post.save()
  return HttpResponseRedirect(reverse('homepage'))

def sort_view(request):
  posts = sorted(Post.objects.all(), key= lambda post: post.votes(), reverse=True)
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
  return render(request, 'add_post.html', {'form': form})




def edit_post(request, post_id: int):
  posts = Post.objects.get(id=post_id)
  if request.method == 'POST':
    form = AddPostForm(request.POST, instance=posts)
    if form.is_valid():
      form.save()
    return HttpResponseRedirect(reverse('homepage'))
  form = AddPostForm(instance=posts)
  return render(request, 'generic_form.html', {'form': form})


def delete_post(request, post_id: int):
  post = Post.objects.get(id=post_id)
  post.delete()
  return HttpResponseRedirect(reverse('homepage'))


# def images_view(request):
#   if request.method == 'POST':
#     form = ImgForm(request.POST, request.FILES)
#     if form.is_valid():
#       form.save()
#       return redirect('success')
#   else:
#     form = ImgForm()
#     return render(request, 'index.html', {'form': form})

# def success(request):
#   return HttpResponse('Successfully Uploaded')


# def show_images(request):
#   if request.method == 'GET':
#     images = Images.objects.all()
#     return render(request, 'display_images.html', {'images': images})
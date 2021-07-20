from django.db.models import fields
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponseRedirect, reverse
from post_app.models import Post
from post_app.forms import AddPostForm, PostDeleteForm
from django.contrib.auth.decorators import login_required
from subreddit.models import SubReddit, Moderator
from comments.models import Comment
from comments.forms import AddCommentForm
from user_app.models import RedditUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


class indexView(View):
  def get(self,request):
    template_name = 'index.html'
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, template_name, context)

@login_required
def upvote_view(request, post_id: int):
  post = Post.objects.get(id=post_id)
  post.upvotes += 1
  post.save()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('homepage')))



@login_required
def downvote_view(request, post_id: int):
  post = Post.objects.get(id=post_id)
  post.downvotes += 1
  post.save()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('homepage')))

class SortView(View):
  def get(self, request):
    template_name = 'index.html'
    posts = sorted(Post.objects.all(), key= lambda post: post.votes(), reverse=True)
    context = {'posts': posts}
    return render(request, template_name, context)
# def sort_view(request):
#   posts = sorted(Post.objects.all(), key= lambda post: post.votes(), reverse=True)
#   return render(request, 'index.html', {'posts': posts})

class PostDetailView(View):
  def get(self,request, post_id: int):
    template_name = 'post_detail.html'
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    form = AddCommentForm
    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, template_name, context)
# def post_detail(request, post_id: int):
#   post = Post.objects.get(id=post_id)
#   comments = Comment.objects.filter(post=post)
#   form = AddCommentForm()
#   return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})




@login_required
def add_post(request):
  if request.method == 'POST':
    form = AddPostForm(request.POST, request.FILES)
    if form.is_valid():
      data = form.cleaned_data
      post = form.save(commit=False)
      post.author = request.user
      post.save()
    return HttpResponseRedirect(reverse('homepage'))
  form = AddPostForm()
  return render(request, 'add_post.html', {'form': form})


# def image_upload_view(request):
#   if request.method == 'POST':
#     form = AddPostForm(request.POST, request.FILES)
#     if form.is_valid():
#       form.save()
#       img_obj = form.instance
#       return render(request, 'main.html.html', {'form': form, 'img_obj': img_obj})
#   form = AddPostForm()
#   return render(request, 'main.html', {'form': form})



@login_required
def edit_post(request, post_id: int):
  posts = Post.objects.get(id=post_id)
  if request.method == 'POST':
    form = AddPostForm(request.POST, request.FILES, instance=posts,)
    if form.is_valid():
      form.save()
    return HttpResponseRedirect(reverse('homepage'))
  form = AddPostForm(instance=posts)
  return render(request, 'add_post.html', {'form': form})

def postview(request, id, name):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    # This adds a comment to the post
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        user = RedditUser.objects.get(id=request.user.id)
        post = Post.objects.get(id=id)
        if form.is_valid():
            data = form.cleaned_data
            parent_id = request.POST.get('comment_id')
            if parent_id:
                parent = comments.get(id=parent_id)
            else:
                parent = None
            Comment.objects.create(
                body=data['body'],
                user=user,
                post=post,
                parent=parent,
            )
            return HttpResponseRedirect(reverse('postview', kwargs={'name': name, 'id': id}))
    form = AddCommentForm()

    if request.user.is_authenticated:
        moderators = Moderator.objects.filter(user=request.user)
        moderators = [moderator.user for moderator in moderators]
        commentator = Comment.objects.filter(user=request.user)
        commentator = [c.user for c in commentator]
    else:
        moderators = None
        commentator = None
    return render(request, 'post.html', {'post': post, 'comments': comments, 
    'form': form, "moderators":moderators, "commentator": commentator})


# def delete_view(request, id):
    # post = Post.objects.get(id=id)
    # form = PostDeleteForm()
    # data = form.cleaned_data
    # post.type_post = data['type_post']
    # post.content = data['data']
    # post.url_post = data['url_post']
    # post.image = data['image']
    # post.save()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_view(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('homepage'))

def image_url(self):
  if self.image:
    return self.image.url
  return '#'



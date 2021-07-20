from post_app.models import Post
from comments.forms import AddCommentForm, DeleteCommentForm
from django.shortcuts import HttpResponseRedirect
from comments.models import Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, HttpResponseRedirect, reverse





@login_required
def up_vote(request, comment_id):
    up_post = Comment.objects.get(id=comment_id)
    up_post.upvotes += 1
    up_post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def down_vote(request,comment_id):
    down_post = Comment.objects.get(id=comment_id)
    down_post.downvotes += 1
    down_post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def edit_comment(request, comment_id: int):
  comments = Comment.objects.get(id=comment_id)
  if request.method == 'POST':
    form = AddCommentForm(request.POST, instance=comments,)
    if form.is_valid():
      form.save()
    return HttpResponseRedirect(reverse('homepage'))
  form = AddCommentForm(instance=comments)
  return render(request, 'generic_form.html', {'form': form})

# have an if satement checking if it is a moderator or not.
# def delete_view(request, comment_id):
#     comment = Comment.objects.get(id=comment_id)
#     form = DeleteCommentForm()
#     data = form.cleaned_data
#     comment.body = data['body']
#     comment.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def addcomment(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.method == 'POST':
    form = AddCommentForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
    return HttpResponseRedirect(reverse('homepage'))
  form = AddCommentForm()
  return render(request, 'add_post.html', {'form': form})




def deletecomment(request, comment_id: int):
  comment = Comment.objects.get(id=comment_id)
  comment.delete()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
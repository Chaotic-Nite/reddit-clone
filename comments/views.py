from comments.forms import DeleteCommentForm
from django.shortcuts import HttpResponseRedirect
from comments.models import Comment
from django.contrib.auth.decorators import login_required


@login_required
def up_vote(request, name, id, id2):
    up_post = Comment.objects.get(id=id2)
    up_post.upvotes += 1
    up_post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def down_vote(request, name, id, id2):
    down_post = Comment.objects.get(id=id2)
    down_post.downvotes += 1
    down_post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# have an if satement checking if it is a moderator or not.
def delete_view(request, id):
    comment = Comment.objects.get(id=id)
    form = DeleteCommentForm()
    data = form.cleaned_data
    comment.body = data['body']
    comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

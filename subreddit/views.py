from django.shortcuts import render, reverse, HttpResponseRedirect
from subreddit.models import SubReddit,Moderator
from subreddit.forms import AddSubRedditForm
from user_app.models import RedditUser
from post_app.models import Post
from subreddit.models import Moderator
from django.contrib.auth.decorators import login_required


@login_required
def add_subreddit(request):
    if request.method == "POST":
        form = AddSubRedditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            subreddit = SubReddit.objects.create(
                name=data['name'],
                description=data['description'],
            )
            Moderator.objects.get_or_create(
                user=request.user,
                is_moderator=True,
            )
            subscriber = RedditUser.objects.get(id=request.user.id)
            moderator = Moderator.objects.filter(user=request.user).first()
            subscriber.sub_reddits.add(subreddit)
            # subreddit.moderator.add(moderator)
            subreddit.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AddSubRedditForm()

    return render(request, 'generic_form.html', {"form": form})


def subredditview(request, name):
    subreddit = SubReddit.objects.get(name=name)
    posts = Post.objects.filter(subreddit=subreddit.id)
    if request.user.is_authenticated:
        moderators = Moderator.objects.filter(user=request.user)
        moderators = [moderator.user for moderator in moderators]
    else:
        moderators = None
    current_path = f'/r/{subreddit.name}/'
    
    subscribe_list = request.user.sub_reddits.all()
    return render(request, 'subreddit/subreddit.html', {"subreddit": subreddit, "posts": posts, "current_path": current_path,"moderators": moderators, "subscribe_list": subscribe_list})


@login_required
def subscribe(request, id):
    # have it in Reddituser insted of SubReddit
    subreddit = SubReddit.objects.get(id=id)
    subscriber = RedditUser.objects.get(id=request.user.id)
    subscriber.sub_reddits.add(subreddit)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def unsubscribe(request, id):
     # have it in Reddituser insted of SubReddit
    subreddit = SubReddit.objects.get(id=id)
    subscriber = RedditUser.objects.get(id=request.user.id)
    subscriber.sub_reddits.remove(subreddit)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# # have to work on this
def subredditnew(request, name):
    subreddit = SubReddit.objects.get(name=name)
    posts = Post.objects.filter(subreddit=subreddit.id).order_by("-date_created")
    if request.user.is_authenticated:
        moderators = Moderator.objects.filter(user=request.user)
        moderators = [moderator.user for moderator in moderators]
    else:
        moderators = None
    new_path = f'/r/{subreddit.name}/new/'
    subscribe_list = SubReddit.objects.filter(subscriber=request.user.id)
    return render(request, 'subreddit.html', {'posts': posts, 'subreddit': subreddit, "new_path": new_path,"moderators": moderators, "subscribe_list": subscribe_list})


def subreddithot(request, name):
    subreddit = SubReddit.objects.get(name=name)
    posts = Post.objects.filter(subreddit=subreddit.id).order_by("-score")
    if request.user.is_authenticated:
        moderators = Moderator.objects.filter(user=request.user)
        moderators = [moderator.user for moderator in moderators]
    else:
        moderators = None
    hot_path = f'/r/{subreddit.name}/hot/'
    subscribe_list = SubReddit.objects.filter(subscriber=request.user.id)
    return render(request, 'subreddit.html', {'posts': posts, 'subreddit': subreddit, "hot_path": hot_path,"moderators": moderators, "subscribe_list": subscribe_list})
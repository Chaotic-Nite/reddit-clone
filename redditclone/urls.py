from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from post_app import views as post_view
from user_app import views as user_view
from comments import views as comment_view
from subreddit import views as subreddit_view


urlpatterns = [
    path('admin/', admin.site.urls),
    # Comments
    path('comment/upvote/<int:comment_id>/', comment_view.up_vote, name='comment_upvote'),
    path('comment/downvote/<int:comment_id>/', comment_view.down_vote, name='comment_downvote'),
    path('comment/edit/<int:comment_id>/', comment_view.edit_comment),
    path('comment/delete/<int:comment_id>/', comment_view.deletecomment, name='delete_comment'),
    path('comment/add/<int:post_id>/', comment_view.addcomment),
    # Posts
    path('post/<int:post_id>', post_view.PostDetailView.as_view(), name='post_detail'),
    path('addpost/', post_view.add_post),
    path('upvote/<int:post_id>/', post_view.upvote_view, name='upvote'),
    path('downvote/<int:post_id>/', post_view.downvote_view, name='downvote'),
    path('post/<int:id>/delete/', post_view.delete_view, name='post_delete'),
    path('sorted/', post_view.SortView.as_view()),
    path('post/<int:post_id>/edit/', post_view.edit_post),
    # path('upload', post_view.image_upload_view),
    # Users
    path('signup/', user_view.signup_view, name='signup'),
    path('login/', user_view.login_view, name='login'),
    path('logout/', user_view.LogOutView.as_view(), name='logout'),
    path('new/', user_view.new, name='new'),
    path('hot/', user_view.hot, name='hot'),
    path('following/', user_view.following, name="following"),
    path('', user_view.index, name='homepage'),
    # Subreddits
    path('addsubreddit/', subreddit_view.add_subreddit, name='addsubreddit'),
    path('r/<str:name>/', subreddit_view.subredditview, name='subreddit'),
    path('r/<str:name>/new/', subreddit_view.subredditnew, name='subredditnew'),
    path('r/<str:name>/hot/', subreddit_view.subreddithot, name='subreddithot'),
    path('subscribed/<int:id>/', subreddit_view.subscribe, name='subscribe'),
    path('unsubscribed/<int:id>/', subreddit_view.unsubscribe, name='unsubscribe'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
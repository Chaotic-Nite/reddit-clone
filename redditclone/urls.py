"""redditclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from post_app import views
from user_app import views as views2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
    path('addpost/', views.add_post),
    path('upvote/<int:post_id>/', views.upvote_view, name='upvote'),
    path('downvote/<int:post_id>/', views.downvote_view, name='downvote'),
    path('sorted/', views.sort_view),
    path('post/<int:post_id>/delete/', views.delete_post),
    path('post/<int:post_id>/edit/', views.edit_post),
    path('signup/', views2.signup_view, name='signup'),
    path('login/', views2.login_view, name='login'),
    path('logout/', views2.logout_view, name='logout'),
    path('', views.index, name='homepage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
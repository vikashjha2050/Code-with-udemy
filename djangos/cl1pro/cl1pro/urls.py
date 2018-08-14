"""cl1pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import blviews
from django.contrib.auth import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',blviews.bloglist.as_view(),name='home'),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^post_new/',blviews.createpost.as_view(),name='post_new'),
    url(r'^detail/(?P<pk>\d+)$',blviews.detailpost.as_view(),name='detail'),
    url(r'^update/(?P<pk>\d+)',blviews.updatepost.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)',blviews.deletepost.as_view(),name='delete'),
    url(r'^publish/(?P<pk>\d+)',blviews.publishpost,name='publish'),
    url(r'^drafts/',blviews.draftpost.as_view(),name='drafts'),
    url(r'^detail/(?P<pk>\d+)/add_comment/$',blviews.add_comment_fun,name='add_comment'),
    url(r'^commentd/(?P<pk>\d+)/approve_comment/$',blviews.approve_comment_fun,name='approve_comment'),
    url(r'^commentd/(?P<pk>\d+)/delete_comment/$',blviews.delete_comment_fun,name='delete_comment'),


]

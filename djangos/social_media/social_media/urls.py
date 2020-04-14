"""social_media URL Configuration

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
from social_media import views, api
from accounts import acviews
from django.contrib.auth import views as auth_views
from groups import gviews
from posts.poviews import create_post
from rest_framework.routers import DefaultRouter
from django.urls import include, path

router = DefaultRouter()
router.register(r'groupsapi', api.GroupViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home_fun.as_view(),name='home' ),
    url(r'^user/$',views.my_profile.as_view(),name='my_profile' ),
    url(r'^signup/$',acviews.signup.as_view(),name='signup' ),
    url(r"login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"thanks/$", acviews.thanks.as_view(), name="thanks"),
    url(r'^create_group/$',gviews.create_group.as_view(),name='create_group' ),
    url(r'^groups-list$',gviews.groups_list.as_view(),name='groups_list' ),
    url(r'^group_detail/(?P<pk>\d+)/$',gviews.group_detail.as_view(),name='group_detail' ),
    url(r'^group_detail/(?P<pk>\d+)/join$',gviews.group_join,name='group_join' ),
    url(r'^group_detail/(?P<pk>\d+)/leave$',gviews.group_leave,name='group_leave' ),
    url(r'^create_post/$',create_post,name='create_post' ),
    url('', include(router.urls)),
    path('groupapi/<pk>', api.GroupViews.as_view(), name='group-generic-apiview' ),
    path('groupapi/<pk>', api.GroupGenericApi.as_view(), name='group-generic-apiview' ),


]

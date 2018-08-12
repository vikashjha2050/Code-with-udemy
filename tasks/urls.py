"""tasks URL Configuration

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
from task1 import views
from basicforms import formviews
from relative_url import relviews
from templateinheri import inheriviews
from filterapp import filterviews
from usermodel1 import umviews
from cbvhello import cbvviews

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^user/',views.userfun),
    url(r'^admin/', admin.site.urls),
    url(r'^formpage/',formviews.form_view_fun),
    url(r'^relative/',relviews.rel_view_fun),
    url(r'^base/',relviews.rel_base_fun,name='rel_base_fun'),
    url(r'^inheritance/',inheriviews.inheri_fun),
    url(r'^filter/',filterviews.filter_fun),
    url(r'^reg/',umviews.um_register),
    url(r'^log/',umviews.user_login,name='log'),
    url(r'^cbv1/',cbvviews.cbv1fun.as_view()),
    url(r'^cbv2/',cbvviews.cbv2fun.as_view()),
    url(r'^sclist$',cbvviews.cbvlistclass.as_view()),
    url(r'^(?P<pk>\d+)/$',cbvviews.cbvdetailclass.as_view(),name='detail'),
    url(r'^cbvcreate/$',cbvviews.cbvcreateclass.as_view()),
    url(r'^update/(?P<pk>\d+)$',cbvviews.cbvupdateclass.as_view(),name='update'),

]

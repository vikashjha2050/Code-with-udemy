from django.views.generic import ListView
from posts.models import post
from groups.models import group, group_members

class home_fun(ListView):
     model=post
     template_name='home.html'
     def get_queryset(self):
         
         return post.objects.filter(user=self.request.user)

class my_profile(ListView):
     model=post
     template_name='user.html'
     def get_queryset(self):
        print post.objects.filter(user=self.request.user)
        return post.objects.filter(user=self.request.user)

from django.views.generic import ListView
from posts.models import Post

class home_fun(ListView):
	model = Post
	template_name='home.html'

	def get_queryset(self):
		x = Post.objects.values('user_id').distinct().count()
		print(x) 
		return Post.objects.all()

class my_profile(ListView):
	model = Post
	template_name='user.html'
	
	def get_queryset(self):
		return Post.objects.filter(user=self.request.user)

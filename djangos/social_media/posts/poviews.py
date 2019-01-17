# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404,redirect
from posts.models import post
from posts.forms import PostForm
from django.contrib.auth.models import User

# Create your views here.

def create_post(request):
    user_id = request.user.id
    username1 = User.objects.get(id=user_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect('group_detail', pk=post.groupname.pk)
        else:
            print("form is not valid")
    else:
        form = PostForm(initial={'user': username1})
    return render(request, 'posts/post_form.html', {'form': form})

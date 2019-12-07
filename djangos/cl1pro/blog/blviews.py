# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog,Comment
from django.urls import reverse
from django.utils import timezone
from blog.forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class bloglist(ListView):
     model=Blog
     template_name='blog/home.html'
     def get_queryset(self):
        return Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class draftpost(ListView):
     model=Blog
     template_name='blog/home.html'
     def get_queryset(self):
        return Blog.objects.filter(published_date__isnull=True).order_by('created_date')

class createpost(CreateView):
    model=Blog
    fields=('author','title','text')
    success_url="/"

class detailpost(DetailView):
    context_object_name = 'post_details'
    model=Blog
    template_name='blog/detailpost.html'

class updatepost(UpdateView):
    model=Blog
    fields=('author','title','text')
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

class deletepost(DeleteView):
    context_object_name = 'post_details'
    model=Blog
    success_url='/'

@login_required
def publishpost(request,pk):
    blog1 = get_object_or_404(Blog, pk=pk)
    blog1.publish()
    return redirect('detail', pk=pk)

@login_required
def add_comment_fun(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save(request)
            return redirect('detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def approve_comment_fun(request, pk):
    commentob = get_object_or_404(Comment, pk=pk)
    commentob.approve()
    return redirect('detail', pk=commentob.post.pk)

@login_required
def delete_comment_fun(request, pk):
    commentob = get_object_or_404(Comment, pk=pk)
    commentob.delete()
    return redirect('detail', pk=commentob.post.pk)

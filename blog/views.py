from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog
from django.contrib import messages

def post_list(request):
    queryset_list = Blog.objects.all().order_by('-created')
    query = request.GET.get('q')
    if query:
        queryset_list = Blog.objects.all().filter(title__icontains=query)

    return render(request, 'index.html', {'blog':queryset_list})

class DetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'

class PostCreateView(CreateView):
    model = Blog
    fields = [
        'title',
        'content',
    ]
    template_name = "blog/new_post.html"

    

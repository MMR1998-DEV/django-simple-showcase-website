from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'posts': blogs})


def details(request, blog_id):
    blog_post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog_post': blog_post})

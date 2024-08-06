from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog(request, cat_name = None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context=context)

def blog_single(request, pid):
    post = get_object_or_404(Post,pk=pid, status=1)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context=context)


def blog_category(request, cat_name): # we can use just one view def blog
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name) # catgory -> get us id -> with __ we can extract fields like name
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context=context)

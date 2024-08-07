from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# def blog(request, cat_name = None, author_username = None):
def blog(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'] )

    #add paginator
    posts = Paginator(posts, 1)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(posts.num_pages) # get last page

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

def blog_search(request):
    # print(request.__dict__)
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'): # varlus feture s:= if condition true
            posts = posts.filter(content__contains=s) # contains for search query in context
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context=context)
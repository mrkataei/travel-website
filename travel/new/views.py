from django.shortcuts import render
from blog.models import Post

def home(request):
    posts = Post.objects.filter(status=1).order_by('published_date')[:6]
    context = {'posts': posts}
    return render(request, 'new/index.html', context=context)

def about(request):
    return render(request, 'new/about.html')

def contact(request):
    return render(request, 'new/contact.html')
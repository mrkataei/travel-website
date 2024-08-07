from django.shortcuts import render, HttpResponse
from blog.models import Post
from new.forms import ContactForm

def home(request):
    posts = Post.objects.filter(status=1).order_by('published_date')[:6]
    context = {'posts': posts}
    return render(request, 'new/index.html', context=context)

def about(request):
    return render(request, 'new/about.html')

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            form.save()
        #     return HttpResponse('done')
        # else:
        #     return HttpResponse('not valid ') # in html use {%csrf_token%}{{form }}
        
    form = ContactForm()
    return render(request, 'new/contact.html',{'form': form} )
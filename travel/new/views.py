from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home(request):
    return render(request, 'new/index.html')

def about(request):
    return render(request, 'new/about.html')

def contact(request):
    return render(request, 'new/contact.html')
from django.urls import path
from new.views import home, about, contact, newsletter

app_name = 'new'
urlpatterns = [
    path('', home, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('newsletter', newsletter, name='newsletter'),
]

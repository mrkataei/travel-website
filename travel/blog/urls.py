from django.urls import path
from blog.views import blog, blog_single, blog_category

app_name = 'blog'
urlpatterns = [
    path('', blog, name='blog'),
    path('category/<str:cat_name>', blog_category, name='category'),
    path('post-<int:pid>', blog_single, name='single'),
]

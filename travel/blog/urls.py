from django.urls import path
from blog.views import blog, blog_single, blog_category, blog_search

app_name = 'blog'
urlpatterns = [
    path('', blog, name='blog'),
    # path('category/<str:cat_name>', blog_category, name='category'), # exampla when we two vies for this aim
    path('category/<str:cat_name>', blog, name='category'),
    path('author/<str:author_username>', blog, name='author'),
    path('search/', blog_search, name='search'),
    path('post-<int:pid>', blog_single, name='single'),
]

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class Post(models.Model):
    image = models.ImageField(upload_to= 'blog/', default='blog\default.jpg') # default uploads to media\blog
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    title = models.CharField(max_length=250)
    content = models.TextField()
    #tag
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.title
    

    def get_parents(self):
        return ",".join([str(p) for p in self.category.all()])
    

    def snippets(self):
        return self.content[:100] + "..." # you can use truncatechar tag filter
        # like this -> {{post.content|truncatechar:100}}

    def get_absolute_url(self):
        return reverse("blog:single", kwargs={'pid': self.id})
    
    class Meta: # apply to all objects but when define it into admin just view in admin panel not in queries
        ordering = ['created_date']



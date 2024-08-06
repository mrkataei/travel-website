from django import template
from blog.models import Post, Category

register = template.Library()

#simple tags

@register.simple_tag(name="totalposts")
def function():
    posts = Post.objects.filter(status = 1).count()
    return posts


# in html use this -> {% totalposts as tp %} -> {{tp }}


@register.simple_tag(name="posts")
def function():
    posts = Post.objects.filter(status = 1)
    return posts

#filter tags

@register.filter
def snippet(value, arg= 100):
    return value[:arg] + "..."

# in html {{post.content|snippet:arg}}

#inclusion tags


@register.inclusion_tag('blog/latest-posts.html')
def latestposts(arg = 3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {"posts": posts}


# in html {% latestposts %}


@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status = 1)
    categories = Category.objects.all()
    cat_dict = {}

    for cat in categories:
        cat_dict[cat] = posts.filter(category=cat).count()

    return {'categories': cat_dict}
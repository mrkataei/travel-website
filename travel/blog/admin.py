from django.contrib import admin
from blog.models import Post, Category

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title', )
    # exclude = ('title', )
    list_display = ('title', 'counted_views', 'status', 'published_date', 'created_date', 'get_parents')
    list_filter = ('status', )
    # ordering = ['-created_date']
    search_fields = ['title', 'content']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
